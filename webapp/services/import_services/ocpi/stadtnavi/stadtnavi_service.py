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
from webapp.services.import_services.base_import_service import BaseImportService
from webapp.services.import_services.ocpi.ocpi_mapper import OcpiMapper
from webapp.services.import_services.ocpi.ocpi_validators import LocationInput, OcpiInput


class StadtnaviImportService(BaseImportService):

    ocpi_validator: OcpiInput = DataclassValidator(OcpiInput)
    location_validator: LocationInput = DataclassValidator(LocationInput)
    ocpi_mapper = OcpiMapper()

    def download_and_save(self):
        input_dict = self.remote_helper.get(
            remote_server_type=RemoteServerType.STADTNAVI,
            path='/herrenberg/charging-stations/charging-stations-ocpi.json',
        )

        input_data = self.ocpi_validator.validate(input_dict)

        exceptions = []
        location_updates = []
        for location_dict in input_data.data:
            try:
                location_input = self.location_validator.validate(location_dict)
            except ValidationError as exception:
                exceptions.append((input_data, exception))
                continue
            location_updates.append(self.ocpi_mapper.map_location(location_input, 'stadtnavi'))
        self.save_location_updates(location_updates, 'stadtnavi')

