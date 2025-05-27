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
from validataclass.validators import DataclassValidator

from webapp.common.error_handling.exceptions import RemoteException
from webapp.common.logging.models import LogMessageType
from webapp.models.source import SourceStatus
from webapp.services.import_services.base_import_service import BaseImportService, SourceInfo
from webapp.services.import_services.models import EvseUpdate, LocationUpdate

from .validators import EVSEDataRecord, EVSEStatusRecord, OpendataSwissRealtimeInput, OpendataSwissStaticInput

logger = logging.getLogger(__name__)


class OpendataSwissImportService(BaseImportService, ABC):
    opendata_swiss_static_validator = DataclassValidator(OpendataSwissStaticInput)
    opendata_swiss_realtime_validator = DataclassValidator(OpendataSwissRealtimeInput)
    evse_data_record_validator = DataclassValidator(EVSEDataRecord)
    evse_status_record_validator = DataclassValidator(EVSEStatusRecord)

    source_info = SourceInfo(
        uid='opendata_swiss',
        name='OpenData Swiss',
        public_url='https://opendata.swiss/de/dataset/ladestationen-fuer-elektroautos',
        has_realtime_data=True,
    )

    def fetch_static_data(self):
        source = self.get_source()
        error_count = 0
        success_count = 0
        location_updates: list[LocationUpdate] = []
        static_data_updated_at = datetime.now(timezone.utc)

        try:
            raw_opendata_swiss_data = self.json_request(
                url='https://data.geo.admin.ch/ch.bfe.ladestellen-elektromobilitaet/data/oicp/ch.bfe.ladestellen-elektromobilitaet.json',
            )
        except RemoteException as e:
            logger.error(
                f'opendata swiss static data request failed: {e}',
                extra={'attributes': {'type': LogMessageType.IMPORT_SOURCE}},
            )
            self.update_source(source, static_status=SourceStatus.FAILED, realtime_status=SourceStatus.FAILED)
            return

        try:
            opendata_swiss_input: OpendataSwissStaticInput = self.opendata_swiss_static_validator.validate(
                raw_opendata_swiss_data,
            )
        except ValidationError as e:
            logger.error(
                f'opendata swiss static data {raw_opendata_swiss_data} has validation error: {e.to_dict()}',
                extra={'attributes': {'type': LogMessageType.IMPORT_SOURCE}},
            )
            self.update_source(source, static_status=SourceStatus.FAILED, realtime_status=SourceStatus.FAILED)
            return

        for evse_data in opendata_swiss_input.EVSEData:
            location_updates_by_uid: dict[str, LocationUpdate] = {}
            for raw_evse_data_record in evse_data.EVSEDataRecord:
                try:
                    evse_data_record: EVSEDataRecord = self.evse_data_record_validator.validate(raw_evse_data_record)
                except ValidationError as e:
                    logger.warning(
                        f'opendata swiss EVSEDataRecord {raw_evse_data_record} has error: {e.to_dict()}',
                        extra={'attributes': {'type': LogMessageType.IMPORT_SOURCE}},
                    )
                    error_count += 1
                    continue

                # Ability to filter for countries
                filter_countries: list[str] | None = self.config.get('filter_countries')
                if filter_countries and evse_data_record.Address.Country not in filter_countries:
                    continue

                location_updates_by_uid[evse_data_record.GeoCoordinates.Google] = evse_data_record.to_location_update(
                    location_update=location_updates_by_uid.get(evse_data_record.GeoCoordinates.Google),
                    operator_name=evse_data.OperatorName,
                )

            location_updates += list(location_updates_by_uid.values())
            success_count += 1

        self.save_location_updates(location_updates)

        self.update_source(
            source=source,
            static_status=SourceStatus.ACTIVE,
            static_error_count=error_count,
            static_data_updated_at=static_data_updated_at,
        )
        logger.info(
            f'Successfully updated {self.source_info.uid} static data with {success_count} valid '
            f'locations and {error_count} failed locations.',
            extra={'attributes': {'type': LogMessageType.IMPORT_LOCATION}},
        )

    def fetch_realtime_data(self):
        source = self.get_source()
        # Don't fetch realtime updates if there is no static data
        if source.static_status != SourceStatus.ACTIVE:
            return

        evse_updates: list[EvseUpdate] = []
        success_count = 0
        error_count = 0
        realtime_data_updated_at = datetime.now(timezone.utc)

        try:
            raw_opendata_swiss_data = self.json_request(
                url='https://data.geo.admin.ch/ch.bfe.ladestellen-elektromobilitaet/status/oicp/ch.bfe.ladestellen-elektromobilitaet.json',
            )
            opendata_swiss_input: OpendataSwissRealtimeInput = self.opendata_swiss_realtime_validator.validate(
                raw_opendata_swiss_data,
            )
        except (ValidationError, RemoteException) as e:
            logger.error(
                f'opendata swiss realtime data has error: {e.to_dict()}',
                extra={'attributes': {'type': LogMessageType.IMPORT_SOURCE}},
            )
            self.update_source(source, static_status=SourceStatus.FAILED, realtime_status=SourceStatus.FAILED)
            return

        for evse_status in opendata_swiss_input.EVSEStatuses:
            for raw_evse_status_record in evse_status.EVSEStatusRecord:
                try:
                    evse_status_record: EVSEStatusRecord = self.evse_status_record_validator.validate(
                        raw_evse_status_record,
                    )
                except ValidationError as e:
                    logger.warning(
                        f'opendata swiss EVSEStatusRecord {raw_evse_status_record} has error: {e.to_dict()}',
                        extra={'attributes': {'type': LogMessageType.IMPORT_SOURCE}},
                    )
                    error_count += 1
                    continue

                evse_updates.append(evse_status_record.to_evse_update())
                success_count += 1

        self.save_evse_updates(evse_updates)

        self.update_source(
            source=source,
            realtime_status=SourceStatus.ACTIVE,
            realtime_error_count=error_count,
            realtime_data_updated_at=realtime_data_updated_at,
        )

        logger.info(
            f'Successfully updated {self.source_info.uid} ealtime with {success_count} valid '
            f'locations and {error_count} failed locations.',
            extra={'attributes': {'type': LogMessageType.IMPORT_LOCATION}},
        )
