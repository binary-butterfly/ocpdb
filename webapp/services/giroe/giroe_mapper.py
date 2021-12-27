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

from math import sqrt
from hashlib import sha256
from typing import Optional
from flask import Config, current_app
from webapp.services.generic.SaveLocation import LocationUpdate
from webapp.services.generic.SaveChargepoint import ChargepointUpdate
from webapp.services.generic.SaveConnector import ConnectorUpdate
from webapp.enums import ChargepointStatus, ConnectorFormat, ConnectorType, Capability, PowerType
from .giroe_validator import LocationInput, StationInput, ConnectorInput


class GiroeMapper:
    amperage_factor = {
        PowerType.DC: 400,
        PowerType.AC_3_PHASE: 400 * sqrt(3),
        PowerType.AC_1_PHASE: 230
    }

    def __init__(self, config: Optional[Config] = None):
        self._config = config

    @property
    def config(self):
        return self._config if self._config else current_app.config

    def hash_object_id(self, object_type: str, object_id: int) -> str:
        return sha256(('%s-%s-%s' % (object_type, object_id, self.config['OBJECT_ID_SECRET'])).encode()).hexdigest()[:32]

    def map_location_input_to_update(self, location_data: LocationInput) -> LocationUpdate:
        location_update = LocationUpdate(
            source='giroe',
            uid=self.hash_object_id('location', location_data.id),
            address=location_data.address,
            city=location_data.locality,
            postal_code=location_data.postalcode,
            country=location_data.country,
            lat=location_data.lat,
            lon=location_data.lon,
            last_updated=location_data.modified,
            chargepoints=[]
        )
        for station_input in location_data.stations:
            for connector_input in station_input.connectors:
                location_update.chargepoints.append(
                    self.map_station_connector_to_evse_connector(station_input, connector_input)
                )
        return location_update

    def map_station_connector_to_evse_connector(self, station_input: StationInput, connector_input: ConnectorInput):
        return ChargepointUpdate(
            source='giroe',
            uid=self.hash_object_id('evse', connector_input.id),
            evse_id=connector_input.uid,
            status=connector_input.status,
            capabilities=[
                Capability.UNLOCK_CAPABLE,
                Capability.RFID_READER,
                Capability.CONTACTLESS_CARD_SUPPORT,
                Capability.DEBIT_CARD_PAYABLE,
                Capability.REMOTE_START_STOP_CAPABLE
            ],
            last_updated=connector_input.modified,
            connectors=[ConnectorUpdate(
                source='giroe',
                uid=self.hash_object_id('connector', connector_input.id),
                standard=connector_input.standard,
                format=connector_input.format,
                max_voltage=230 if connector_input.power_type == PowerType.AC_1_PHASE else 400,
                max_electric_power=connector_input.power
            )]
        )
