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

from webapp.repositories import EvseRepository, LocationRepository, ObjectNotFoundException
from webapp.server_rest_api.base_handler import ServerApiBaseHandler
from webapp.services.import_services.giroe import GiroeImportService
from webapp.services.import_services.giroe.giroe_validator import LocationInput
from .giroe_validator import ConnectorPatchInput
from ...models import Location


class GiroeHandler(ServerApiBaseHandler):
    evse_repository: EvseRepository
    giroe_import_service: GiroeImportService

    def __init__(
            self,
            *args,
            location_repository: LocationRepository,
            evse_repository: EvseRepository,
            giroe_import_service: GiroeImportService,
            **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.location_repository = location_repository
        self.evse_repository = evse_repository
        self.giroe_import_service = giroe_import_service

    def handle_put_location(self, location_id: int, location_input: LocationInput):

        location_uid = self.giroe_import_service.giroe_mapper.hash_object_id('location', location_id)

        try:
            location = self.location_repository.fetch_location_by_uid('giroe', location_uid)

            if not location_input.public:
                self.location_repository.delete_location(location)
                return

        except ObjectNotFoundException:
            pass

        location_update = self.giroe_import_service.giroe_mapper.map_location_input_to_update(location_input)

        self.giroe_import_service.save_location_update('giroe', location_update)

    def handle_delete_location(self, location_id: int):
        location_uid = self.giroe_import_service.giroe_mapper.hash_object_id('location', location_id)

        location = self.location_repository.fetch_location_by_uid('giroe', location_uid)

        self.location_repository.delete_location(location)

    def handle_patch_connector(self, connector_uid: str, connector_input: ConnectorPatchInput):
        evse = self.evse_repository.fetch_by_uid(source='giroe', uid=connector_uid)

        evse.status = connector_input.status
        evse.last_updated = connector_input.modified

        self.evse_repository.save_evse(evse)
