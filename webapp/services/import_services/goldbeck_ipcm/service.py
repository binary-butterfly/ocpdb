"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2025 binary butterfly GmbH

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

import logging
from abc import ABC
from datetime import datetime, timezone

from validataclass.exceptions import ValidationError
from validataclass.validators import AnythingValidator, DataclassValidator, ListValidator

from webapp.common.error_handling.exceptions import RemoteException
from webapp.common.logging.models import LogMessageType
from webapp.models.source import Source, SourceStatus
from webapp.services.import_services.base_import_service import BaseImportService, SourceInfo
from webapp.services.import_services.goldbeck_ipcm.validators import GoldbeckIpcmChargePoint
from webapp.services.import_services.models import EvseUpdate, LocationUpdate

logger = logging.getLogger(__name__)


class GoldbeckIpcmImportService(BaseImportService, ABC):
    list_validator: list[dict] = ListValidator(AnythingValidator(allowed_types=[dict]))
    chargepoint_validator = DataclassValidator(GoldbeckIpcmChargePoint)

    def fetch_static_data(self):
        source = self.get_source()
        location_updates_by_uid: dict[str, LocationUpdate] = {}

        static_data_updated_at = datetime.now(timezone.utc)

        chargepoints, static_error_count = self._fetch_chargepoints(source)

        for chargepoint in chargepoints:
            location_update = chargepoint.to_location_update(
                location_update=location_updates_by_uid.get(str(chargepoint.postalAddress.id)),
            )
            location_updates_by_uid[str(chargepoint.postalAddress.id)] = location_update

        location_updates: list[LocationUpdate] = list(location_updates_by_uid.values())
        self.save_location_updates(location_updates)

        self.update_source(
            source=source,
            static_status=SourceStatus.ACTIVE,
            static_error_count=static_error_count,
            static_data_updated_at=static_data_updated_at,
        )
        logger.info(
            f'Successfully updated {self.source_info.uid} static with {len(location_updates)} valid locations and '
            f'{static_error_count} failed locations.',
            extra={'attributes': {'type': LogMessageType.IMPORT_LOCATION}},
        )

    def fetch_realtime_data(self):
        source = self.get_source()
        # Don't fetch realtime updates if there is no static data
        if source.static_status != SourceStatus.ACTIVE:
            return

        evse_updates: list[EvseUpdate] = []
        realtime_error_count = 0
        realtime_data_updated_at = datetime.now(timezone.utc)

        chargepoints, static_error_count = self._fetch_chargepoints(source)

        for chargepoint in chargepoints:
            evse_updates += chargepoint.to_realtime_evse_updates()

        self.save_evse_updates(evse_updates)

        self.update_source(
            source=source,
            realtime_status=SourceStatus.ACTIVE,
            realtime_error_count=realtime_error_count,
            realtime_data_updated_at=realtime_data_updated_at,
        )
        logger.info(
            f'Successfully updated {self.source_info.uid} realtime with {len(evse_updates)} valid EVSEs '
            f'and {realtime_error_count} failed EVSEs.',
            extra={'attributes': {'type': LogMessageType.IMPORT_LOCATION}},
        )

    def _fetch_chargepoints(self, source: Source) -> tuple[list[GoldbeckIpcmChargePoint], int]:
        chargepoints: list[GoldbeckIpcmChargePoint] = []
        error_count = 0

        try:
            chargepoint_list = self.json_request(
                auth=(self.config.get('user'), self.config.get('password')),
            )
            chargepoint_dicts = self.list_validator.validate(chargepoint_list)
        except (ValidationError, RemoteException) as e:
            logger.error(
                f'goldbeck ipcm data has error: {e.to_dict()}',
                extra={'attributes': {'type': LogMessageType.IMPORT_SOURCE}},
            )
            self.update_source(source, static_status=SourceStatus.FAILED, realtime_status=SourceStatus.FAILED)
            raise  # TODO

        for chargepoint_dict in chargepoint_dicts:
            try:
                chargepoint: GoldbeckIpcmChargePoint = self.chargepoint_validator.validate(chargepoint_dict)
                chargepoints.append(chargepoint)
            except ValidationError as e:
                logger.warning(
                    f'goldbeck ipcm chargepoint has error: {e.to_dict()}',
                    extra={'attributes': {'type': LogMessageType.IMPORT_SOURCE}},
                )
                error_count += 1
                continue

        return chargepoints, error_count


class HeilbronnNeckarbogenImportService(GoldbeckIpcmImportService):
    source_info = SourceInfo(
        uid='heilbronn_neckarbogen',
        name='Heilbronn Neckarbogen',
        public_url='https://www.heilbronn.de/bauen-wohnen/stadtquartier-neckarbogen.html',
        source_url='https://control.goldbeck-parking.de/ipaw/services/charging/v1x0/charging-stations?maxResults=1000',
        has_realtime_data=True,
    )
