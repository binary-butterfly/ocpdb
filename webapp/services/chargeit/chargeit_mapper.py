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

from decimal import Decimal
from datetime import datetime,timezone
from validataclass.helpers import UnsetValue
from webapp.services.generic.SaveLocation import LocationUpdate
from webapp.services.generic.SaveChargepoint import ChargepointUpdate
from webapp.services.generic.SaveConnector import ConnectorUpdate
from webapp.enums import ChargepointStatus, ConnectorFormat, ConnectorType
from .chargeit_validators import LocationInput, CircuitInput, CircuitStatus, Plug


class ChargeitMapper:
    def map_location_to_location(self, location_input: LocationInput):
        location_update = LocationUpdate(
            source='chargeit',
            uid=location_input.shortcode,
            name=location_input.name,
            address=location_input.address.street,
            postal_code=location_input.address.zipCode,
            city=location_input.address.city,
            lat=Decimal(location_input.lat),
            lon=Decimal(location_input.lon),
            country='DE',
            last_updated=datetime.utcnow().replace(tzinfo=timezone.utc),
            twentyfourseven=UnsetValue if location_input.hours is UnsetValue else location_input.hours.twentyfourseven,
            #description=location_input.description  TODO: handle descriptions,
            chargepoints=[self.map_circuit_to_chargepoint(circuit_input) for circuit_input in location_input.circuits]
        )
        # TODO: regular hours
        return location_update

    def map_circuit_to_chargepoint(self, circuit_input: CircuitInput):
        return ChargepointUpdate(
            source='chargeit',
            uid=circuit_input.evseId,
            evse_id=circuit_input.evseId,
            status=self.map_status(circuit_input.status),
            last_updated=datetime.utcnow().replace(tzinfo=timezone.utc),
            connectors=[
                ConnectorUpdate(
                    source='chargeit',
                    uid=str(circuit_input._id),
                    max_electric_power=circuit_input.max_electric_power,
                    format=self.map_format(circuit_input.plug),
                    standard=self.map_standard(circuit_input.plug)
                )
            ]
        )

    def map_status(self, circuit_status: CircuitStatus) -> ChargepointStatus:
        return {
            CircuitStatus.OCPP_AVAILABLE: ChargepointStatus.AVAILABLE,
            CircuitStatus.OCPP_OCCUPIED: ChargepointStatus.CHARGING,
            CircuitStatus.OCPP16_FINSISHING: ChargepointStatus.CHARGING,
            CircuitStatus.OCPP16_CHARGING: ChargepointStatus.CHARGING,
            CircuitStatus.IDLE: ChargepointStatus.CHARGING,
            CircuitStatus.CHARGING: ChargepointStatus.CHARGING,
            CircuitStatus.OCPP_FAULTED: ChargepointStatus.OUTOFORDER,
            CircuitStatus.STATE_CHARGING_PLUG_REMOVE: ChargepointStatus.CHARGING,
            CircuitStatus.CHARGING_PAUSE: ChargepointStatus.CHARGING
        }.get(circuit_status, ChargepointStatus.UNKNOWN)

    def map_format(self, circuit_plug: Plug) -> ConnectorFormat:
        if circuit_plug == Plug.TYP2_CABLE:
            return ConnectorFormat.CABLE
        return ConnectorFormat.SOCKET

    def map_standard(self, curcuit_plug: Plug) -> ConnectorType:
        return {
            Plug.SCHUKO: ConnectorType.DOMESTIC_F,
            Plug.TYP2: ConnectorType.IEC_62196_T2,
            Plug.TYP2_11KW: ConnectorType.IEC_62196_T2,
            Plug.TYP2_14KW: ConnectorType.IEC_62196_T2,
            Plug.TYP2_39KW: ConnectorType.IEC_62196_T2,
            Plug.TYP2_CABLE: ConnectorType.IEC_62196_T2,
            Plug.CCS: ConnectorType.IEC_62196_T2_COMBO,
            Plug.CHAdeMO: ConnectorType.CHADEMO,
            Plug.CEE: ConnectorType.IEC_60309_2_three_32
        }.get(curcuit_plug, ConnectorType.IEC_62196_T2)
