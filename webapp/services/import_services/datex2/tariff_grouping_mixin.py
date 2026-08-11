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
from collections.abc import Iterable, Iterator
from dataclasses import asdict, fields
from datetime import datetime
from hashlib import sha256
from typing import NamedTuple

from webapp.common.json import DefaultJSONEncoder
from webapp.common.logging.models import LogMessageType
from webapp.services.import_services.models import (
    EvseUpdate,
    LocationUpdate,
    SourceInfo,
    TariffAssociationUpdate,
    TariffUpdate,
)

logger = logging.getLogger(__name__)

# Everything else on a TariffUpdate defines what the customer pays and therefore takes part in the
# comparison. The uid is just an identifier, and last_updated is merged to the newest value of a
# group instead of separating tariffs which charge the same fees.
_IDENTITY_ONLY_TARIFF_FIELDS = frozenset({'uid', 'last_updated'})

# The tariff of an association takes part in the comparison as its fingerprint instead of its raw
# content, so it is dropped here as well. start_date_time is merged to the oldest value of a group,
# just like last_updated is merged to the newest one.
_IDENTITY_ONLY_TARIFF_ASSOCIATION_FIELDS = frozenset({'uid', 'tariff', 'start_date_time', 'last_updated'})


class TariffGroupingResult(NamedTuple):
    tariff_count: int
    tariff_association_count: int


class _TariffAssociationGroup(NamedTuple):
    tariff_fingerprint: str
    tariff_association_updates: list[TariffAssociationUpdate]


class TariffGroupingMixin(ABC):
    source_info: SourceInfo

    def group_identical_tariffs(self, location_updates: list[LocationUpdate]) -> TariffGroupingResult:
        """
        Collapse tariffs and tariff associations with identical content and return how many remain.

        DATEX2 publishes the tariff of every EVSE separately, so an operator running a single price list
        across its whole network produces one tariff and one tariff association per EVSE. This keeps one
        tariff per group of identical tariffs and one association per group of identical associations,
        gives both a uid which is a fingerprint of their content and hands the survivors back to every
        EVSE of the group. The duplicates are dropped right here, so they never reach the database, while
        every EVSE keeps its link to the tariffs which apply to it.

        Two tariffs are identical if all their fee-defining values match: the tariff elements (including
        price components, taxes and restrictions), the currency and the tariff type. Two associations are
        identical if they point at the same grouped tariff and address the same audience. Neither the uids
        nor the timestamps take part in the comparison; the survivors are stamped with the newest
        last_updated of their group, associations additionally with the oldest start_date_time, which is
        when the first EVSE of the group started to charge these fees.
        """
        tariff_updates_by_fingerprint: dict[str, list[TariffUpdate]] = {}
        tariff_association_groups: dict[str, _TariffAssociationGroup] = {}
        # The association fingerprints of every EVSE which has tariffs, in import order, so the grouped
        # associations can be handed back to their EVSEs without fingerprinting everything twice.
        association_fingerprints_by_evse_update: list[tuple[EvseUpdate, list[str]]] = []

        for evse_update in self._iterate_evse_updates(location_updates):
            association_fingerprints: list[str] = []

            for tariff_association_update in evse_update.tariff_association or []:
                tariff_fingerprint = self._build_tariff_fingerprint(tariff_association_update.tariff)
                tariff_updates_by_fingerprint.setdefault(tariff_fingerprint, []).append(
                    tariff_association_update.tariff,
                )

                association_fingerprint = self._build_tariff_association_fingerprint(
                    tariff_association_update,
                    tariff_fingerprint,
                )
                tariff_association_groups.setdefault(
                    association_fingerprint,
                    _TariffAssociationGroup(tariff_fingerprint=tariff_fingerprint, tariff_association_updates=[]),
                ).tariff_association_updates.append(tariff_association_update)

                association_fingerprints.append(association_fingerprint)

            if association_fingerprints:
                association_fingerprints_by_evse_update.append((evse_update, association_fingerprints))

        grouped_tariff_updates = self._group_tariff_updates(tariff_updates_by_fingerprint)
        grouped_tariff_association_updates = self._group_tariff_association_updates(
            tariff_association_groups,
            grouped_tariff_updates,
        )

        for evse_update, association_fingerprints in association_fingerprints_by_evse_update:
            # Two rates of the same EVSE can share a fingerprint, and an EVSE cannot hold the same
            # association twice, so dict.fromkeys drops those duplicates while keeping the order stable.
            evse_update.tariff_association = [
                grouped_tariff_association_updates[association_fingerprint]
                for association_fingerprint in dict.fromkeys(association_fingerprints)
            ]

        tariff_update_count = sum(len(tariff_updates) for tariff_updates in tariff_updates_by_fingerprint.values())
        logger.info(
            f'Grouped {tariff_update_count} {self.source_info.uid} tariffs into '
            f'{len(grouped_tariff_updates)} distinct tariffs and '
            f'{len(grouped_tariff_association_updates)} distinct tariff associations.',
            extra={'attributes': {'type': LogMessageType.IMPORT_SOURCE}},
        )

        return TariffGroupingResult(
            tariff_count=len(grouped_tariff_updates),
            tariff_association_count=len(grouped_tariff_association_updates),
        )

    @classmethod
    def _group_tariff_updates(
        cls,
        tariff_updates_by_fingerprint: dict[str, list[TariffUpdate]],
    ) -> dict[str, TariffUpdate]:
        grouped_tariff_updates: dict[str, TariffUpdate] = {}

        for fingerprint, tariff_updates in tariff_updates_by_fingerprint.items():
            grouped_tariff_update = tariff_updates[0]
            grouped_tariff_update.uid = fingerprint
            grouped_tariff_update.last_updated = cls._newest(
                tariff_update.last_updated for tariff_update in tariff_updates
            )
            grouped_tariff_updates[fingerprint] = grouped_tariff_update

        return grouped_tariff_updates

    @classmethod
    def _group_tariff_association_updates(
        cls,
        tariff_association_groups: dict[str, _TariffAssociationGroup],
        grouped_tariff_updates: dict[str, TariffUpdate],
    ) -> dict[str, TariffAssociationUpdate]:
        grouped_tariff_association_updates: dict[str, TariffAssociationUpdate] = {}

        for fingerprint, tariff_association_group in tariff_association_groups.items():
            tariff_association_updates = tariff_association_group.tariff_association_updates

            grouped_tariff_association_update = tariff_association_updates[0]
            grouped_tariff_association_update.uid = fingerprint
            # The tariff of the group survived the tariff grouping only if it happened to be the first of
            # its group, so the association is pointed at the survivor instead of at its own tariff.
            grouped_tariff_association_update.tariff = grouped_tariff_updates[
                tariff_association_group.tariff_fingerprint
            ]
            grouped_tariff_association_update.last_updated = cls._newest(
                tariff_association_update.last_updated for tariff_association_update in tariff_association_updates
            )
            grouped_tariff_association_update.start_date_time = cls._oldest(
                tariff_association_update.start_date_time for tariff_association_update in tariff_association_updates
            )
            grouped_tariff_association_updates[fingerprint] = grouped_tariff_association_update

        return grouped_tariff_association_updates

    @staticmethod
    def _iterate_evse_updates(location_updates: list[LocationUpdate]) -> Iterator[EvseUpdate]:
        for location_update in location_updates:
            for charging_station_update in location_update.charging_pool:
                yield from charging_station_update.evses

    @classmethod
    def _build_tariff_fingerprint(cls, tariff_update: TariffUpdate) -> str:
        financials = {
            key: value for key, value in asdict(tariff_update).items() if key not in _IDENTITY_ONLY_TARIFF_FIELDS
        }

        return cls._fingerprint(financials)

    @classmethod
    def _build_tariff_association_fingerprint(
        cls,
        tariff_association_update: TariffAssociationUpdate,
        tariff_fingerprint: str,
    ) -> str:
        content = {
            field.name: getattr(tariff_association_update, field.name)
            for field in fields(tariff_association_update)
            if field.name not in _IDENTITY_ONLY_TARIFF_ASSOCIATION_FIELDS
        }
        content['tariff'] = tariff_fingerprint

        return cls._fingerprint(content)

    @staticmethod
    def _fingerprint(content: dict) -> str:
        # sort_keys makes the fingerprint independent of the field order, while list order stays
        # significant because the order of the tariff elements decides which one applies first.
        serialized_content = json.dumps(content, sort_keys=True, cls=DefaultJSONEncoder)

        # Truncated like the per-EVSE uids the mappers generate, which keeps it within Tariff.uid's 64 chars.
        return sha256(serialized_content.encode()).hexdigest()[:32]

    @staticmethod
    def _newest(timestamps: Iterable[datetime | None]) -> datetime | None:
        set_timestamps = [timestamp for timestamp in timestamps if timestamp is not None]

        return max(set_timestamps) if set_timestamps else None

    @staticmethod
    def _oldest(timestamps: Iterable[datetime | None]) -> datetime | None:
        set_timestamps = [timestamp for timestamp in timestamps if timestamp is not None]

        return min(set_timestamps) if set_timestamps else None
