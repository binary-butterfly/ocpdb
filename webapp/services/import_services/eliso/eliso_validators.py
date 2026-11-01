"""
Open ChargePoint DataBase OCPDB
Copyright (C) 2026 binary butterfly GmbH

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
from decimal import Decimal
from enum import Enum

from pycountry import countries
from validataclass.dataclasses import Default, validataclass
from validataclass.validators import (
    DataclassValidator,
    DateTimeValidator,
    EnumValidator,
    FloatToDecimalValidator,
    IntegerValidator,
    ListValidator,
    StringValidator,
)

from webapp.models.connector import ConnectorFormat, ConnectorType, PowerType
from webapp.models.evse import EvseStatus
from webapp.services.import_services.models import (
    BusinessUpdate,
    ChargingStationUpdate,
    ConnectorUpdate,
    EvseRealtimeUpdate,
    EvseUpdate,
    LocationUpdate,
)


class ElisoConnectorType(Enum):
    CCS = 'Combo2/CCS (DC)'
    TYPE_2 = 'Type 2 (AC)'

    def to_connector_type(self) -> ConnectorType:
        return {
            self.CCS: ConnectorType.IEC_62196_T2_COMBO,
            self.TYPE_2: ConnectorType.IEC_62196_T2,
        }.get(self)

    def to_connector_format(self) -> ConnectorFormat:
        return {
            self.CCS: ConnectorFormat.CABLE,
            self.TYPE_2: ConnectorFormat.SOCKET,
        }.get(self)


class ElisoOperationalStatus(Enum):
    OPERATIONAL = 'Operational'
    NON_OPERATIONAL = 'Non-operational'


class ElisoAvailabilityStatus(Enum):
    IN_USE = 'In use'
    NOT_IN_USE = 'Not in use'


@validataclass
class ElisoConnectorInput:
    maxPower: int = IntegerValidator(min_value=0)  # in kW
    powerType: PowerType = EnumValidator(PowerType)
    type_of_connector: ElisoConnectorType = EnumValidator(ElisoConnectorType)


@validataclass
class ElisoEvseInput:
    evseId: str = StringValidator(min_length=1, max_length=48)
    connectors: list[ElisoConnectorInput] = ListValidator(DataclassValidator(ElisoConnectorInput), min_length=1)


@validataclass
class ElisoCoordinatesInput:
    latitude: Decimal = FloatToDecimalValidator(min_value=-90, max_value=90, allow_integers=True)
    longitude: Decimal = FloatToDecimalValidator(min_value=-180, max_value=180, allow_integers=True)


@validataclass
class ElisoLocationInput:
    address: str = StringValidator(min_length=1)
    postalCode: str = StringValidator(min_length=1)
    city: str = StringValidator(min_length=1)
    country_iso_3166_alpha_2: str = StringValidator(min_length=2, max_length=2)
    coordinates: ElisoCoordinatesInput = DataclassValidator(ElisoCoordinatesInput)
    operator_name: str = StringValidator(min_length=1)
    hotline_number: str | None = StringValidator(), Default(None)
    opening_time: str | None = StringValidator(), Default(None)
    mobilithek_last_updated_dts: datetime = DateTimeValidator()
    evses: list[ElisoEvseInput] = ListValidator(DataclassValidator(ElisoEvseInput), min_length=1)

    def to_location_update(self, source_uid: str) -> LocationUpdate:
        # eliso does not provide location ids, so we use the lowest EVSE id as stable identifier
        uid = min(evse.evseId for evse in self.evses)
        return LocationUpdate(
            uid=uid,
            source=source_uid,
            time_zone='Europe/Berlin',
            name=self.address,
            address=self.address,
            postal_code=self.postalCode,
            city=self.city,
            country=countries.get(alpha_2=self.country_iso_3166_alpha_2).alpha_3,
            lat=self.coordinates.latitude,
            lon=self.coordinates.longitude,
            operator=BusinessUpdate(name=self.operator_name),
            help_phone=self.hotline_number,
            twentyfourseven=True if self.opening_time == '24/7' else None,
            last_updated=self.mobilithek_last_updated_dts,
            charging_pool=[
                ChargingStationUpdate(
                    uid=uid,
                    last_updated=self.mobilithek_last_updated_dts,
                    evses=[
                        EvseUpdate(
                            uid=evse.evseId,
                            evse_id=evse.evseId,
                            status=EvseStatus.UNKNOWN,
                            last_updated=self.mobilithek_last_updated_dts,
                            connectors=[
                                ConnectorUpdate(
                                    uid=str(index),
                                    standard=connector.type_of_connector.to_connector_type(),
                                    format=connector.type_of_connector.to_connector_format(),
                                    power_type=connector.powerType,
                                    max_electric_power=connector.maxPower * 1000,
                                    last_updated=self.mobilithek_last_updated_dts,
                                )
                                for index, connector in enumerate(evse.connectors, start=1)
                            ],
                        )
                        for evse in self.evses
                    ],
                ),
            ],
        )


@validataclass
class ElisoEvseStatusInput:
    evseId: str = StringValidator(min_length=1, max_length=48)
    operational_status: ElisoOperationalStatus = EnumValidator(ElisoOperationalStatus)
    availability_status: ElisoAvailabilityStatus | None = EnumValidator(ElisoAvailabilityStatus), Default(None)
    mobilithek_last_updated_dts: datetime = DateTimeValidator()

    def to_evse_realtime_update(self) -> EvseRealtimeUpdate:
        if self.operational_status == ElisoOperationalStatus.NON_OPERATIONAL:
            status = EvseStatus.INOPERATIVE
        elif self.availability_status == ElisoAvailabilityStatus.IN_USE:
            status = EvseStatus.CHARGING
        elif self.availability_status == ElisoAvailabilityStatus.NOT_IN_USE:
            status = EvseStatus.AVAILABLE
        else:
            status = EvseStatus.UNKNOWN

        return EvseRealtimeUpdate(
            uid=self.evseId,
            evse_id=self.evseId,
            status=status,
            last_updated=self.mobilithek_last_updated_dts,
            status_last_updated=self.mobilithek_last_updated_dts,
        )
