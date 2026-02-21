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

from hashlib import sha256
from math import sqrt

from butterfly_pubsub.giroe import ChargeConnectorStatus
from pycountry import countries

from webapp.common.config import ConfigHelper
from webapp.models.charging_station import Capability
from webapp.models.connector import PowerType
from webapp.models.evse import EvseStatus
from webapp.services.import_services.models import ChargingStationUpdate, ConnectorUpdate, EvseUpdate, LocationUpdate

from .giroe_validator import ConnectorInput, LocationInput, StationInput


class GiroeMapper:
    amperage_factor = {
        PowerType.DC: 400,
        PowerType.AC_3_PHASE: 400 * sqrt(3),
        PowerType.AC_1_PHASE: 230,
    }

    def __init__(self, config_helper: ConfigHelper):
        self.config_helper = config_helper

    def hash_object_id(self, object_type: str, object_id: int) -> str:
        hash_content = f'{object_type}-{object_id}-{self.config_helper.get("OBJECT_ID_SECRET")}'

        return sha256(hash_content.encode()).hexdigest()[:32]

    def map_location_input_to_update(self, location_data: LocationInput) -> LocationUpdate:
        location_update = LocationUpdate(
            source='giroe',
            uid=self.hash_object_id('location', location_data.id),
            address=location_data.address,
            city=location_data.locality,
            postal_code=location_data.postalcode,
            country=countries.get(alpha_2=location_data.country).alpha_3,
            lat=location_data.lat,
            lon=location_data.lon,
            last_updated=location_data.modified,
            time_zone='Europe/Berlin',
            charging_pool=[
                self.map_station_input_to_charging_station_update(station_input)
                for station_input in location_data.stations
            ],
        )
        return location_update

    def map_station_input_to_charging_station_update(self, station_input: StationInput) -> ChargingStationUpdate:
        return ChargingStationUpdate(
            uid=station_input.uid,
            evses=[
                self.map_station_connector_to_evse_connector(
                    station_input=station_input,
                    connector_input=connector_input,
                )
                for connector_input in station_input.connectors
            ],
            capabilities=[
                Capability.UNLOCK_CAPABLE,
                Capability.RFID_READER,
                Capability.CONTACTLESS_CARD_SUPPORT,
                Capability.DEBIT_CARD_PAYABLE,
                Capability.REMOTE_START_STOP_CAPABLE,
            ],
            last_updated=station_input.modified,
        )

    def map_station_connector_to_evse_connector(self, station_input: StationInput, connector_input: ConnectorInput):
        return EvseUpdate(
            uid=connector_input.uid,
            evse_id=connector_input.uid,
            status=self.map_charge_connector_status_to_evse_status(connector_input.status),
            last_updated=connector_input.modified,
            connectors=[
                ConnectorUpdate(
                    uid=self.hash_object_id('connector', connector_input.id),
                    standard=connector_input.standard,
                    format=connector_input.format,
                    power_type=connector_input.power_type,
                    max_electric_power=connector_input.power,
                    last_updated=connector_input.modified,
                )
            ],
        )

    @staticmethod
    def map_charge_connector_status_to_evse_status(charge_connector_status: ChargeConnectorStatus) -> EvseStatus:
        return {
            ChargeConnectorStatus.AVAILABLE: EvseStatus.AVAILABLE,
            ChargeConnectorStatus.BLOCKED: EvseStatus.BLOCKED,
            ChargeConnectorStatus.CHARGING: EvseStatus.CHARGING,
            ChargeConnectorStatus.INOPERATIVE: EvseStatus.INOPERATIVE,
            ChargeConnectorStatus.OUTOFORDER: EvseStatus.OUTOFORDER,
            ChargeConnectorStatus.PLANNED: EvseStatus.PLANNED,
            ChargeConnectorStatus.REMOVED: EvseStatus.REMOVED,
            ChargeConnectorStatus.RESERVED: EvseStatus.RESERVED,
            ChargeConnectorStatus.UNKNOWN: EvseStatus.UNKNOWN,
            ChargeConnectorStatus.PREPARING: EvseStatus.CHARGING,
            ChargeConnectorStatus.SUSPENDED_EVSE: EvseStatus.CHARGING,
            ChargeConnectorStatus.SUSPENDED_EV: EvseStatus.CHARGING,
            ChargeConnectorStatus.FINISHING: EvseStatus.CHARGING,
        }.get(charge_connector_status)
