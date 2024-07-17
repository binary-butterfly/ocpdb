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

from datetime import datetime
from typing import List, Optional

from validataclass.exceptions import ValidationError
from validataclass.validators import DataclassValidator

from webapp.common.remote_helper import RemoteServerType
from webapp.services.import_services.base_import_service import BaseImportService

from ..models import LocationUpdate
from .giroe_mapper import GiroeMapper
from .giroe_validator import LocationInput, LocationListInput


class GiroeImportService(BaseImportService):
    giroe_mapper: GiroeMapper
    location_list_validator = DataclassValidator(LocationListInput)
    location_validator = DataclassValidator(LocationInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.giroe_mapper = GiroeMapper(config_helper=self.config_helper)

    def download_and_save(
        self,
        created_since: Optional[datetime] = None,
        created_until: Optional[datetime] = None,
        modified_since: Optional[datetime] = None,
        modified_until: Optional[datetime] = None,
    ):
        location_updates: List[LocationUpdate] = []
        location_list_input: LocationListInput = self.location_list_validator.validate(
            self.remote_helper.get(
                remote_server_type=RemoteServerType.GIROE,
                path='/api/server/v1/charge-locations',
                params={
                    'technical_backend': 'tcc',
                    **({} if created_since is None else {'created_since': created_since}),
                    **({} if created_until is None else {'created_until': created_until}),
                    **({} if modified_since is None else {'modified_since': modified_since}),
                    **({} if modified_until is None else {'modified_until': modified_until}),
                },
            )
        )
        new_location_updates = self.handle_pulled_locations(location_list_input)
        location_updates += new_location_updates

        while location_list_input.next_path:
            location_list_input: LocationListInput = self.location_list_validator.validate(
                self.remote_helper.get(
                    remote_server_type=RemoteServerType.GIROE,
                    path=location_list_input.next_path,
                ),
            )
            self.handle_pulled_locations(location_list_input)

        self.save_location_updates(location_updates, 'giro-e')

    def handle_pulled_locations(self, location_list_input: LocationListInput) -> List[LocationUpdate]:
        location_inputs: List[LocationUpdate] = []
        for location_dict in location_list_input.items:
            try:
                location_input: LocationInput = self.location_validator.validate(location_dict)
            except ValidationError as e:
                self.logger.info(
                    'import-giro-e',
                    f'location {location_dict} has validation error: {e.to_dict()}',
                )
                continue

            if not location_input.public:
                continue

            location_inputs.append(self.giroe_mapper.map_location_input_to_update(location_input))
        return location_inputs
