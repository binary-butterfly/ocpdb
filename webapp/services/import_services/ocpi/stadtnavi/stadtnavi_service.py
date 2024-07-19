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

from validataclass.exceptions import ValidationError
from validataclass.validators import DataclassValidator

from webapp.common.remote_helper import RemoteServerType
from webapp.models.source import SourceStatus
from webapp.services.import_services.base_import_service import BaseImportService, SourceInfo
from webapp.services.import_services.ocpi.ocpi_mapper import OcpiMapper
from webapp.services.import_services.ocpi.ocpi_validators import LocationInput, OcpiInput


class StadtnaviImportService(BaseImportService):

    ocpi_validator = DataclassValidator(OcpiInput)
    location_validator = DataclassValidator(LocationInput)
    ocpi_mapper = OcpiMapper()

    source_info = SourceInfo(
        uid='stadtnavi',
        name='Stadtnavi',
        public_url='https://stadtnavi.de',
        has_realtime_data=True,
    )

    def download_and_save(self):
        source = self.get_source()
        input_dict = self.remote_helper.get(
            remote_server_type=RemoteServerType.STADTNAVI,
            path='/herrenberg/charging-stations/charging-stations-ocpi.json',
        )
        static_error_count: int = 0
        realtime_error_count: int = 0

        try:
            input_data: OcpiInput = self.ocpi_validator.validate(input_dict)
        except ValidationError as e:
            self.logger.info('import-stadtnavi', f'stadtnavi data {input_dict} has validation error: {e.to_dict()}')
            self.update_source(source, static_status=SourceStatus.FAILED, realtime_status=SourceStatus.FAILED)
            return

        location_updates = []
        for location_dict in input_data.data:
            try:
                location_input: LocationInput = self.location_validator.validate(location_dict)
            except ValidationError as e:
                self.logger.info(
                    'import-stadtnavi',
                    f'location {location_dict} has validation error: {e.to_dict()}',
                )
                static_error_count += 1
                realtime_error_count += 1
                continue
            location_updates.append(self.ocpi_mapper.map_location(location_input, self.source_info.uid))

        self.save_location_updates(location_updates)

        self.update_source(source=source, static_error_count=static_error_count, realtime_error_count=realtime_error_count)
