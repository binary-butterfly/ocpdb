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


from webapp.services.base_service import BaseService
from .SaveLocation import upsert_location, LocationUpdate
from .SaveChargepoint import upsert_chargepoint, ChargepointUpdate
from .SaveConnector import upsert_connector
from webapp.repositories import LocationRepository, EvseRepository, ConnectorRepository


class UpdateService(BaseService):
    location_repository: LocationRepository
    evse_repository: EvseRepository
    connector_repository: ConnectorRepository

    def __init__(
            self,
            *args,
            location_repository: LocationRepository,
            evse_repository: EvseRepository,
            connector_repository: ConnectorRepository,
            **kwargs):
        super().__init__(*args, **kwargs)
        self.location_repository = location_repository
        self.evse_repository = evse_repository
        self.connector_repository = connector_repository

    def upsert_location(self, location_update: LocationUpdate):
        location = upsert_location(location_update)
        if not location:
            return
        for chargepoint_update in location_update.chargepoints:
            chargepoint = upsert_chargepoint(chargepoint_update, location)
            if not chargepoint:
                continue
            for connector_update in chargepoint_update.connectors:
                upsert_connector(connector_update, chargepoint)

    def delete_location(self, location_uid):
        self.location_repository.delete_location(
            location=self.location_repository.fetch_location_by_uid(location_uid)
        )
