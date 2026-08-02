"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2026 binary butterfly GmbH

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import json
import logging
from abc import ABC
from collections.abc import Iterator
from dataclasses import asdict
from datetime import datetime
from hashlib import sha256

from webapp.common.json import DefaultJSONEncoder
from webapp.common.logging.models import LogMessageType
from webapp.services.import_services.models import LocationUpdate, SourceInfo, TariffUpdate

logger = logging.getLogger(__name__)

# Everything else on a TariffUpdate defines what the customer pays and therefore takes part in the
# comparison. The uid is just an identifier, and last_updated is merged to the newest value of a
# group instead of separating tariffs which charge the same fees.
_IDENTITY_ONLY_TARIFF_FIELDS = frozenset({'uid', 'last_updated'})


class TariffGroupingMixin(ABC):
    source_info: SourceInfo

    def group_identical_tariffs(self, location_updates: list[LocationUpdate]) -> int:
        """
        Collapse tariffs with identical fees into one tariff and return the number of remaining tariffs.

        DATEX2 publishes the tariff of every EVSE separately, so an operator running a single price list
        across its whole network produces one tariff per EVSE. This rewrites every tariff uid to a
        fingerprint of the tariff's financial content, which makes identical tariffs collapse onto a
        single tariff - and therefore a single database row - while every EVSE keeps its own tariff
        association.

        Two tariffs are identical if all their fee-defining values match: the tariff elements (including
        price components, taxes and restrictions), the currency and the tariff type. Neither the uid nor
        last_updated take part in the comparison; each group is stamped with the newest last_updated of
        its members.
        """
        tariff_updates_by_fingerprint: dict[str, list[TariffUpdate]] = {}

        for tariff_update in self._iterate_tariff_updates(location_updates):
            tariff_updates_by_fingerprint.setdefault(self._build_fingerprint(tariff_update), []).append(tariff_update)

        tariff_update_count = 0
        for fingerprint, tariff_updates in tariff_updates_by_fingerprint.items():
            last_updated = self._newest_last_updated(tariff_updates)
            for tariff_update in tariff_updates:
                tariff_update.uid = fingerprint
                tariff_update.last_updated = last_updated
            tariff_update_count += len(tariff_updates)

        logger.info(
            f'Grouped {tariff_update_count} {self.source_info.uid} tariffs into '
            f'{len(tariff_updates_by_fingerprint)} distinct tariffs.',
            extra={'attributes': {'type': LogMessageType.IMPORT_SOURCE}},
        )

        return len(tariff_updates_by_fingerprint)

    @staticmethod
    def _iterate_tariff_updates(location_updates: list[LocationUpdate]) -> Iterator[TariffUpdate]:
        for location_update in location_updates:
            for charging_station_update in location_update.charging_pool:
                for evse_update in charging_station_update.evses:
                    for tariff_association_update in evse_update.tariff_association or []:
                        yield tariff_association_update.tariff

    @staticmethod
    def _build_fingerprint(tariff_update: TariffUpdate) -> str:
        financials = {
            key: value for key, value in asdict(tariff_update).items() if key not in _IDENTITY_ONLY_TARIFF_FIELDS
        }
        # sort_keys makes the fingerprint independent of the field order, while list order stays
        # significant because the order of the tariff elements decides which one applies first.
        serialized_financials = json.dumps(financials, sort_keys=True, cls=DefaultJSONEncoder)

        # Truncated like the per-EVSE uids the mappers generate, which keeps it within Tariff.uid's 64 chars.
        return sha256(serialized_financials.encode()).hexdigest()[:32]

    @staticmethod
    def _newest_last_updated(tariff_updates: list[TariffUpdate]) -> datetime | None:
        last_updateds = [
            tariff_update.last_updated for tariff_update in tariff_updates if tariff_update.last_updated is not None
        ]

        return max(last_updateds) if last_updateds else None
