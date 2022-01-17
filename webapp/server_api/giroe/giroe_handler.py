# encoding: utf-8

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

from validataclass.validators import DataclassValidator
from ..base_handler import ServerApiBaseHandler
from .giroe_validator import ConnectorPatchInput
from webapp.common.config import ConfigHelper
from webapp.services.giroe.giroe_validator import LocationInput
from webapp.repositories import LocationRepository, EvseRepository, ConnectorRepository
from webapp.repositories.evse_repository import EvseUpdate
from webapp.services.giroe.giroe_mapper import GiroeMapper
from webapp.services.generic.update_service import UpdateService


class GiroeHandler(ServerApiBaseHandler):
    evse_repository: EvseRepository
    connector_patch_validator: DataclassValidator[ConnectorPatchInput] = DataclassValidator(ConnectorPatchInput)
    location_validator: DataclassValidator[LocationInput] = DataclassValidator(LocationInput)
    giroe_mapper: GiroeMapper
    update_service: UpdateService

    def __init__(
            self,
            *args,
            location_repository: LocationRepository,
            evse_repository: EvseRepository,
            connector_repository: ConnectorRepository,
            **kwargs):
        super().__init__(*args, **kwargs)
        self.evse_repository = evse_repository
        self.giroe_mapper = GiroeMapper(config_helper=self.config_helper)
        self.update_service = UpdateService(
            logger=self.logger,
            config_helper=self.config_helper,
            location_repository=location_repository,
            evse_repository=evse_repository,
            connector_repository=connector_repository
        )

    def handle_put_location(self, location_id: int, location_dict: dict):
        location_input = self.location_validator.validate(location_dict)
        if not location_input.publish:
            self.update_service.delete_location(
                self.giroe_mapper.hash_object_id('location', location_id)
            )
            return
        self.update_service.upsert_location(
            location_update=self.giroe_mapper.map_location_input_to_update(
                location_data=location_input
            )
        )

    def handle_delete_location(self, location_id: int):
        self.update_service.delete_location(
            self.giroe_mapper.hash_object_id('location', location_id)
        )

    def handle_patch_connector(self, connector_id: int, connector_dict: dict):
        connector_input = self.connector_patch_validator.validate(connector_dict)

        self.evse_repository.update_evse(
            self.evse_repository.fetch_by_uid(
                source='giroe',
                chargepoint_uid=self.giroe_mapper.hash_object_id('evse', connector_id)
            ),
            EvseUpdate(
                last_updated=connector_input.modified,
                status=connector_input.status
            )
        )


