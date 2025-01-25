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

from datetime import datetime, timezone
from decimal import Decimal

from validataclass.helpers import UnsetValue

from webapp.models.connector import ConnectorFormat, ConnectorType
from webapp.models.evse import EvseStatus
from webapp.services.import_services.models import BusinessUpdate, ConnectorUpdate, EvseUpdate, LocationUpdate

from .chargeit_validators import CircuitInput, CircuitStatus, LocationInput, OperatorInput, Plug


class ChargeitMapper:
    def map_location_to_location_update(
        self,
        operator_input: OperatorInput,
        location_input: LocationInput,
    ) -> LocationUpdate:
        # TODO: regular hours
        return LocationUpdate(
            source='chargeit',
            uid=location_input.shortcode,
            name=location_input.name,
            address=location_input.address.street,
            postal_code=location_input.address.zipCode,
            city=location_input.address.city,
            lat=Decimal(location_input.lat),
            lon=Decimal(location_input.lon),
            country='DEU',
            last_updated=datetime.now(tz=timezone.utc),
            twentyfourseven=UnsetValue if location_input.hours is UnsetValue else location_input.hours.twentyfourseven,
            operator=BusinessUpdate(name=operator_input.operatorName),
            evses=[self.map_circuit_to_evse_update(circuit_input) for circuit_input in location_input.circuits],
        )

    def map_circuit_to_evse_update(self, circuit_input: CircuitInput) -> EvseUpdate:
        return EvseUpdate(
            uid=circuit_input.evseId,
            evse_id=circuit_input.evseId,
            status=self.map_status(circuit_input.status),
            last_updated=datetime.now(tz=timezone.utc),
            connectors=[
                ConnectorUpdate(
                    uid=str(circuit_input._id),
                    max_electric_power=circuit_input.max_electric_power,
                    format=self.map_format(circuit_input.plug),
                    standard=self.map_standard(circuit_input.plug),
                ),
            ],
        )

    @staticmethod
    def map_status(circuit_status: CircuitStatus) -> EvseStatus:
        return {
            CircuitStatus.IDLE: EvseStatus.CHARGING,
            CircuitStatus.CHARGING: EvseStatus.CHARGING,
            CircuitStatus.STATE_CHARGING_PLUG_REMOVE: EvseStatus.CHARGING,
            CircuitStatus.CHARGING_PAUSE: EvseStatus.CHARGING,
            CircuitStatus.OCPP_AVAILABLE: EvseStatus.AVAILABLE,
            CircuitStatus.OCPP_UNAVAILABLE: EvseStatus.INOPERATIVE,
            CircuitStatus.OCPP_FAULTED: EvseStatus.OUTOFORDER,
            CircuitStatus.OCPP_OCCUPIED: EvseStatus.BLOCKED,
            CircuitStatus.OCPP16_AVAILABLE: EvseStatus.AVAILABLE,
            CircuitStatus.OCPP16_PREPARING: EvseStatus.CHARGING,
            CircuitStatus.OCPP16_CHARGING: EvseStatus.CHARGING,
            CircuitStatus.OCPP16_SUSPENDEDEV: EvseStatus.CHARGING,
            CircuitStatus.OCPP16_SUSPENDEDEVSE: EvseStatus.CHARGING,
            CircuitStatus.OCPP16_FINISHING: EvseStatus.CHARGING,
            CircuitStatus.OCPP16_FINSISHING: EvseStatus.CHARGING,
            CircuitStatus.OCPP16_UNAVAILABLE: EvseStatus.INOPERATIVE,
            CircuitStatus.OCPP16_FAULTED: EvseStatus.OUTOFORDER,
        }.get(circuit_status, EvseStatus.UNKNOWN)

    @staticmethod
    def map_format(circuit_plug: Plug) -> ConnectorFormat:
        if circuit_plug == Plug.TYP2_CABLE:
            return ConnectorFormat.CABLE
        return ConnectorFormat.SOCKET

    @staticmethod
    def map_standard(curcuit_plug: Plug) -> ConnectorType:
        return {
            Plug.SCHUKO: ConnectorType.DOMESTIC_F,
            Plug.TYP2: ConnectorType.IEC_62196_T2,
            Plug.TYP2_11KW: ConnectorType.IEC_62196_T2,
            Plug.TYP2_14KW: ConnectorType.IEC_62196_T2,
            Plug.TYP2_39KW: ConnectorType.IEC_62196_T2,
            Plug.TYP2_CABLE: ConnectorType.IEC_62196_T2,
            Plug.CCS: ConnectorType.IEC_62196_T2_COMBO,
            Plug.CHAdeMO: ConnectorType.CHADEMO,
            Plug.CEE: ConnectorType.IEC_60309_2_three_32,
        }.get(curcuit_plug, ConnectorType.IEC_62196_T2)
