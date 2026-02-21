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
from decimal import Decimal

from butterfly_pubsub.giroe import ChargeConnectorStatus
from validataclass.dataclasses import Default, DefaultUnset, validataclass
from validataclass.helpers import OptionalUnset
from validataclass.validators import (
    AnythingValidator,
    BooleanValidator,
    DataclassValidator,
    DateTimeValidator,
    DecimalValidator,
    EnumValidator,
    IntegerValidator,
    ListValidator,
    Noneable,
    StringValidator,
)

from webapp.models.connector import ConnectorFormat, ConnectorType, PowerType
from webapp.models.evse import EvseStatus


@validataclass
class ConnectorInput:
    id: int = IntegerValidator(min_value=1)
    created: datetime = DateTimeValidator()
    modified: datetime = DateTimeValidator()
    uid: str = StringValidator()
    ocpp_connector_id: int = IntegerValidator()
    status: ChargeConnectorStatus = EnumValidator(ChargeConnectorStatus)
    power: int = IntegerValidator()
    power_type: PowerType = EnumValidator(PowerType)
    standard: ConnectorType = EnumValidator(ConnectorType)
    format: ConnectorFormat = EnumValidator(ConnectorFormat)
    meter_public_key: str | None = Noneable(StringValidator(multiline=True)), Default(None)
    meter_serial_number: str | None = Noneable(StringValidator()), Default(None)


@validataclass
class ConnectorPatchInput(ConnectorInput):
    modified: OptionalUnset[datetime] = DefaultUnset
    uid: OptionalUnset[str] = DefaultUnset
    ocpp_connector_id: OptionalUnset[int] = DefaultUnset
    status: OptionalUnset[EvseStatus] = DefaultUnset
    power: OptionalUnset[int] = DefaultUnset
    power_type: OptionalUnset[PowerType] = DefaultUnset
    standard: OptionalUnset[ConnectorType] = DefaultUnset
    format: OptionalUnset[ConnectorFormat] = DefaultUnset
    meter_public_key: OptionalUnset[str] = DefaultUnset
    meter_serial_number: OptionalUnset[str] = DefaultUnset


@validataclass
class StationInput:
    id: int = IntegerValidator(min_value=1)
    created: datetime = DateTimeValidator()
    modified: datetime = DateTimeValidator()
    uid: str = StringValidator(max_length=36)
    technical_backend: str = StringValidator()
    hardware_id: int = IntegerValidator()
    connectors: list[ConnectorInput] = ListValidator(DataclassValidator(ConnectorInput))


@validataclass
class LocationInput:
    id: int = IntegerValidator(min_value=1)
    created: datetime = DateTimeValidator()
    modified: datetime = DateTimeValidator()
    lat: Decimal = DecimalValidator(min_value=Decimal(-90), max_value=Decimal(90))
    lon: Decimal = DecimalValidator(min_value=Decimal(-180), max_value=Decimal(180))
    address: str = StringValidator()
    postalcode: str = StringValidator()
    locality: str = StringValidator()
    country: str = StringValidator()
    public: bool = BooleanValidator()
    public_description: str = StringValidator(multiline=True)
    stations: list[StationInput] = ListValidator(DataclassValidator(StationInput))


@validataclass
class ItemListInput:
    items: list[dict] = ListValidator(AnythingValidator(allowed_types=[dict]))
    next_path: str | None = StringValidator(), Default(None)
