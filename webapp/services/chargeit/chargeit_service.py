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

from webapp.common.remote_helper import RemoteServerType
from validataclass.exceptions import ValidationError
from validataclass.validators import DataclassValidator

from webapp.services.external_helper import ExternalHelper
from webapp.services.base_service import BaseService
from webapp.services.generic.update_service import UpdateService
from webapp.repositories import LocationRepository, EvseRepository, ConnectorRepository
from .chargeit_mapper import ChargeitMapper
from .chargeit_validators import ChargeitInput, LocationInput


class ChargeitService(BaseService):
    update_service: UpdateService
    external_helper: ExternalHelper = ExternalHelper()
    chargit_mapper: ChargeitMapper = ChargeitMapper()
    chargeit_validator: DataclassValidator[ChargeitInput] = DataclassValidator(ChargeitInput)
    location_validator: DataclassValidator[LocationInput] = DataclassValidator(LocationInput)


    def __init__(
            self,
            *args,
            location_repository: LocationRepository,
            evse_repository: EvseRepository,
            connector_repository: ConnectorRepository,
            **kwargs):
        super().__init__(*args, **kwargs)
        self.update_service = UpdateService(
            logger=self.logger,
            config_helper=self.config_helper,
            location_repository=location_repository,
            evse_repository=evse_repository,
            connector_repository=connector_repository,
        )

    def download_and_save(self):
        exceptions = self.save(
            self.validate(
                self.download()
            )
        )
        if len(exceptions):
            self.logger.error(
                'chargeit',
                'invalid datasets',
                details="\n\n".join(["%s\n%s\n" % (location, exception.to_dict()) for location, exception in exceptions])
            )

    def download(self) -> dict:
        return self.external_helper.get(RemoteServerType.CHARGEIT)

    def validate(self, chargeit_dict: dict) -> ChargeitInput:
        return self.chargeit_validator.validate(chargeit_dict)

    def save(self, chargeit_input: ChargeitInput):
        exceptions = []
        for location_dict in chargeit_input.operator.operatorPlaces:
            try:
                location_input = self.validate_location(location_dict)
            except ValidationError as exception:
                exceptions.append(exception)
                continue

            if not location_input.published:
                self.update_service.delete_location(location_input.shortcode)
                continue

            self.save_location(location_input)
        return exceptions

    def validate_location(self, location_dict: dict) -> LocationInput:
        return self.location_validator.validate(location_dict)

    def save_location(self, location_input: LocationInput):
        self.update_service.upsert_location(
            self.chargit_mapper.map_location_to_location(location_input)
        )
