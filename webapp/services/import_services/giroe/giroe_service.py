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

from webapp.common.remote_helper import RemoteException, RemoteServerType
from webapp.models.source import SourceStatus
from webapp.services.import_services.base_import_service import BaseImportService, SourceInfo

from ..models import LocationUpdate
from .giroe_mapper import GiroeMapper
from .giroe_validator import LocationInput, LocationListInput


class GiroeImportService(BaseImportService):
    giroe_mapper: GiroeMapper
    location_list_validator = DataclassValidator(LocationListInput)
    location_validator = DataclassValidator(LocationInput)

    source_info = SourceInfo(
        uid='giroe',
        name='GLS Mobility GmbH',
        public_url='https://www.gls-mobility.de',
        has_realtime_data=True,
    )

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
        source = self.get_source()
        location_updates: List[LocationUpdate] = []
        static_error_count = 0

        try:
            location_list_data = self.remote_helper.get(
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
            location_list_input: LocationListInput = self.location_list_validator.validate(location_list_data)
        except (ValidationError, RemoteException) as e:
            self.logger.info('import-giro-e', f'giro-e static data has error: {e.to_dict()}')
            self.update_source(source, static_status=SourceStatus.FAILED)
            return

        location_dicts: List[dict] = location_list_input.items

        while location_list_input.next_path:
            try:
                location_list_data = self.remote_helper.get(
                    remote_server_type=RemoteServerType.GIROE,
                    path=location_list_input.next_path,
                )
                location_list_input: LocationListInput = self.location_list_validator.validate(location_list_data)
                location_dicts += location_list_input.items
            except (ValidationError, RemoteException) as e:
                self.logger.info('import-giro-e', f'giro-e static data has error: {e.to_dict()}')
                self.update_source(source, static_status=SourceStatus.FAILED)
                return

        for location_dict in location_dicts:
            try:
                location_input: LocationInput = self.location_validator.validate(location_dict)
            except ValidationError as e:
                self.logger.info(
                    'import-giro-e',
                    f'location {location_dict} has validation error: {e.to_dict()}',
                )
                static_error_count += 1
                continue

            if not location_input.public:
                continue

            location_updates.append(self.giroe_mapper.map_location_input_to_update(location_input))

        self.save_location_updates(location_updates)

        self.update_source(source=source, static_error_count=static_error_count)
