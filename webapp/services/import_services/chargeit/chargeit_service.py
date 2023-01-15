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
from .chargeit_mapper import ChargeitMapper
from .chargeit_validators import ChargeitInput, LocationInput


class ChargeitImportService(BaseImportService):
    chargit_mapper: ChargeitMapper = ChargeitMapper()
    chargeit_validator: DataclassValidator[ChargeitInput] = DataclassValidator(ChargeitInput)
    location_validator: DataclassValidator[LocationInput] = DataclassValidator(LocationInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def download_and_save(self):
        input_dict = self.remote_helper.get(remote_server_type=RemoteServerType.CHARGEIT, path='/ps/rest/feed')

        input_data = self.chargeit_validator.validate(input_dict)

        exceptions = []
        location_updates = []
        for location_dict in input_data.operator.operatorPlaces:
            try:
                location_input = self.location_validator.validate(location_dict)
            except ValidationError as exception:
                exceptions.append((input_data, exception))
                continue

            # don't add unpublished location to list, then it will be removed afterwards if it still is in db
            if not location_input.published:
                continue

            location_updates.append(self.chargit_mapper.map_location_to_location_update(
                operator_input=input_data.operator,
                location_input=location_input,
            ))

        self.save_location_updates(location_updates, 'chargeit')
