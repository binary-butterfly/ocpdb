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

from datetime import datetime
from typing import Optional, List, Tuple
from webapp.common.remote_helper import RemoteServerType
from validataclass.exceptions import ValidationError
from validataclass.validators import DataclassValidator
from webapp.services.external_helper import ExternalHelper
from webapp.services.base_service import BaseService
from webapp.services.generic.update_service import UpdateService
from webapp.common.config import ConfigHelper
from .giroe_mapper import GiroeMapper
from .giroe_validator import LocationListInput, LocationInput
from webapp.repositories import LocationRepository, EvseRepository, ConnectorRepository


class GiroeService(BaseService):
    update_service: UpdateService
    external_helper: ExternalHelper = ExternalHelper()
    giroe_mapper: GiroeMapper
    location_list_validator: DataclassValidator[LocationListInput] = DataclassValidator(LocationListInput)
    location_validator: DataclassValidator[LocationInput] = DataclassValidator(LocationInput)

    def __init__(
            self,
            *args,
            config_helper: ConfigHelper,
            location_repository: LocationRepository,
            evse_repository: EvseRepository,
            connector_repository: ConnectorRepository,
            **kwargs):
        super().__init__(*args, config_helper=config_helper, **kwargs)
        self.update_service = UpdateService(
            logger=self.logger,
            config_helper=config_helper,
            location_repository=location_repository,
            evse_repository=evse_repository,
            connector_repository=connector_repository
        )
        self.giroe_mapper = GiroeMapper(config_helper=self.config_helper)

    def download_and_save(
            self,
            created_since: Optional[datetime] = None,
            created_until: Optional[datetime] = None,
            modified_since: Optional[datetime] = None,
            modified_until: Optional[datetime] = None):
        # TODO: use parameter
        # TODO: check delete
        exceptions = []
        location_list_input = self.location_list_validator.validate(
            self.external_helper.get(
                remote_server_type=RemoteServerType.GIROE,
                path='/api/server/v1/charge-locations?technical_backend=tcc'
            )
        )
        exceptions += self.handle_pulled_locations(location_list_input)

        while location_list_input.next_path:
            location_list_input = self.location_list_validator.validate(
                self.external_helper.get(
                    remote_server_type=RemoteServerType.GIROE,
                    path=location_list_input.next_path
                )
            )
            exceptions += self.handle_pulled_locations(location_list_input)
        if len(exceptions):
            self.logger.error(
                'giroe',
                'invalid datasets',
                details="\n\n".join(["%s\n%s\n" % (location, exception.to_dict()) for location, exception in exceptions])
            )

    def handle_pulled_locations(self, location_list_input: LocationListInput) -> List[Tuple[dict, ValidationError]]:
        exceptions = []
        for location_dict in location_list_input.items:
            try:
                location_input = self.location_validator.validate(location_dict)
                if location_input.publish:
                    self.update_service.upsert_location(
                        self.giroe_mapper.map_location_input_to_update(
                            location_input
                        )
                    )
                    continue
                self.update_service.delete_location(
                    self.giroe_mapper.hash_object_id('location', location_input.id)
                )
            except ValidationError as exception:
                exceptions.append((location_dict, exception))
        return exceptions
