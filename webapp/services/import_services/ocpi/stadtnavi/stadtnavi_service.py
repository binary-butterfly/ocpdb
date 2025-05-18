"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2021 binary butterfly GmbH

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
from datetime import datetime, timezone

from validataclass.exceptions import ValidationError
from validataclass.validators import DataclassValidator

from webapp.common.error_handling.exceptions import RemoteException
from webapp.common.logging.models import LogMessageType
from webapp.models.source import SourceStatus
from webapp.services.import_services.base_import_service import BaseImportService, SourceInfo
from webapp.services.import_services.ocpi.ocpi_mapper import OcpiMapper
from webapp.services.import_services.ocpi.ocpi_validators import LocationInput, OcpiInput

logger = logging.getLogger(__name__)


class StadtnaviImportService(BaseImportService):
    ocpi_validator = DataclassValidator(OcpiInput)
    location_validator = DataclassValidator(LocationInput)
    ocpi_mapper = OcpiMapper()

    source_info = SourceInfo(
        uid='ocpi_stadtnavi',
        name='Stadtnavi',
        public_url='https://stadtnavi.de',
        source_url='https://api.stadtnavi.de/herrenberg/charging-stations/charging-stations-ocpi.json',
        has_realtime_data=True,
    )

    def fetch_static_data(self):
        self.download_and_save()

    def fetch_realtime_data(self):
        self.download_and_save()

    def download_and_save(self):
        source = self.get_source()
        data_updated_at = datetime.now(timezone.utc)
        success_count: int = 0
        error_count: int = 0
        try:
            input_dict = self.json_request()
        except RemoteException as e:
            logger.error(
                f'stadtnavi request failed: {e.to_dict()}',
                extra={'attributes': {'type': LogMessageType.IMPORT_SOURCE}},
            )
            self.update_source(source, static_status=SourceStatus.FAILED, realtime_status=SourceStatus.FAILED)
            return

        try:
            input_data: OcpiInput = self.ocpi_validator.validate(input_dict)
        except ValidationError as e:
            logger.error(
                f'stadtnavi data {input_dict} has validation error: {e.to_dict()}',
                extra={'attributes': {'type': LogMessageType.IMPORT_SOURCE}},
            )
            self.update_source(source, static_status=SourceStatus.FAILED, realtime_status=SourceStatus.FAILED)
            return

        location_updates = []
        for location_dict in input_data.data:
            try:
                location_input: LocationInput = self.location_validator.validate(location_dict)
            except ValidationError as e:
                logger.warning(
                    f'location {location_dict} has validation error: {e.to_dict()}',
                    extra={'attributes': {'type': LogMessageType.IMPORT_LOCATION}},
                )
                error_count += 1
                continue

            location_updates.append(self.ocpi_mapper.map_location(location_input, self.source_info.uid))
            success_count += 1

        self.save_location_updates(location_updates)

        self.update_source(
            source=source,
            static_status=SourceStatus.ACTIVE,
            static_error_count=error_count,
            static_data_updated_at=data_updated_at,
            realtime_status=SourceStatus.ACTIVE,
            realtime_error_count=error_count,
            realtime_data_updated_at=data_updated_at,
        )

        logger.info(
            f'Successfully updated {self.source_info.uid} static and realtime with {success_count} valid '
            f'locations and {error_count} failed locations. .',
            extra={'attributes': {'type': LogMessageType.IMPORT_LOCATION}},
        )
