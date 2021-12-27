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
from webapp.repositories.evse_repository import EvseRepository, EvseUpdate
from webapp.services.giroe.giroe_mapper import GiroeMapper


class GiroeHandler(ServerApiBaseHandler):
    evse_repository: EvseRepository
    connector_patch_validator: DataclassValidator[ConnectorPatchInput] = DataclassValidator(ConnectorPatchInput)
    giroe_mapper: GiroeMapper = GiroeMapper()

    def __init__(self, *args, evse_repository: EvseRepository, **kwargs):
        super().__init__(*args, **kwargs)
        self.evse_repository = evse_repository

    def handle_patch_connector(self, connector_id: int, connector_dict: dict):
        connector_input = self.connector_patch_validator.validate(connector_dict)

        self.evse_repository.update_evse(
            self.evse_repository.fetch_by_uid(
                'giroe',
                self.giroe_mapper.hash_object_id('evse', connector_id)
            ),
            EvseUpdate(
                last_modified=connector_input.modified,
                status=connector_input.status
            )
        )


