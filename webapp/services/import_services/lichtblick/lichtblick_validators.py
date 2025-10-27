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

from datetime import time
from enum import Enum

from validataclass.dataclasses import Default, DefaultUnset, validataclass
from validataclass.helpers import OptionalUnsetNone
from validataclass.validators import (
    AnythingValidator,
    BooleanValidator,
    DataclassValidator,
    EnumValidator,
    FloatValidator,
    IntegerValidator,
    ListValidator,
    Noneable,
    StringValidator,
    TimeFormat,
    TimeValidator,
)

from webapp.common.validation import NoneableToUnsetValue


class Plug(Enum):
    SCHUKO = 'SCHUKO'
    TYP2 = 'TYP2'
    TYP2_11KW = 'TYP2_11KW'
    TYP2_14KW = 'TYP2_14KW'
    TYP2_39KW = 'TYP2_39KW'
    TYP2_CABLE = 'TYP2_CABLE'
    CCS = 'CCS'
    CHAdeMO = 'CHAdeMO'
    GBT_AC = 'GBT_AC'
    GBT_DC = 'GBT_DC'
    CEE = 'CEE'
    UNKNOWN = 'UNKNOWN'


class CircuitStatus(Enum):
    OCPP_AVAILABLE = 'OCPP_AVAILABLE'
    OCPP_OCCUPIED = 'OCPP_OCCUPIED'
    OCPP_UNAVAILABLE = 'OCPP_UNAVAILABLE'
    OCPP_FAULTED = 'OCPP_FAULTED'

    OCPP16_AVAILABLE = 'OCPP16_AVAILABLE'
    OCPP16_PREPARING = 'OCPP16_PREPARING'
    OCPP16_CHARGING = 'OCPP16_CHARGING'
    OCPP16_SUSPENDEDEV = 'OCPP16_SUSPENDEDEV'
    OCPP16_SUSPENDEDEVSE = 'OCPP16_SUSPENDEDEVSE'
    OCPP16_FINISHING = 'OCPP16_FINISHING'
    OCPP16_FINSISHING = 'OCPP16_FINSISHING'
    OCPP16_RESERVED = 'OCPP16_RESERVED'
    OCPP16_UNAVAILABLE = 'OCPP16_UNAVAILABLE'
    OCPP16_FAULTED = 'OCPP16_FAULTED'

    IDLE = 'IDLE'
    CHARGING = 'CHARGING'
    STATE_CHARGING_PLUG_REMOVE = 'STATE_CHARGING_PLUG_REMOVE'
    CHARGING_PAUSE = 'CHARGING_PAUSE'


class PowerInfo(Enum):
    AC_022kW_032A = 'AC_022kW_032A'
    AC_044kW_064A = 'AC_044kW_064A'
    DC_050kW = 'DC_050kW'
    DC_150kW = 'DC_150kW'
    OTHER = 'OTHER'


class LocationStatus(Enum):
    OK = 'OK'
    ATTENTION = 'ATTENTION'
    WARNING = 'WARNING'
    CRITICAL = 'CRITICAL'


class PowerType(Enum):
    AC = 'AC'
    DC = 'DC'


class AccessibilityType(Enum):
    RESTRICTED = 'RESTRICTED'
    PAYINGPUBLIC = 'PAYINGPUBLIC'
    FREEPUBLIC = 'FREEPUBLIC'


@validataclass
class CircuitInput:
    _id: int = IntegerValidator()
    charging: bool = BooleanValidator()
    ready: bool = BooleanValidator()
    powerInfo: PowerInfo = EnumValidator(PowerInfo)
    plug: Plug = EnumValidator(Plug)
    evseId: str = StringValidator()
    status: CircuitStatus = EnumValidator(CircuitStatus)
    isReady: bool = BooleanValidator()
    isCharging: bool = BooleanValidator()
    power_type: PowerType = EnumValidator(PowerType)
    max_electric_power: int = IntegerValidator()


@validataclass
class RegularHours:
    weekdayFrom: int = IntegerValidator()
    weekdayTo: int = IntegerValidator()
    period_begin: time = TimeValidator(TimeFormat.NO_SECONDS)
    period_end: time = TimeValidator(TimeFormat.NO_SECONDS)


@validataclass
class Hours:
    twentyfourseven: bool = BooleanValidator()
    regular_hours: OptionalUnsetNone[list[RegularHours]] = (
        NoneableToUnsetValue(ListValidator(DataclassValidator(RegularHours))),
        DefaultUnset(),
    )


@validataclass
class AddressInput:
    street: str = StringValidator()
    city: str = StringValidator()
    zipCode: str = StringValidator()


@validataclass
class LocationInput:
    name: str = StringValidator()
    serviceTag: str = StringValidator()
    circuits: list[CircuitInput] = ListValidator(DataclassValidator(CircuitInput))
    description: OptionalUnsetNone[str] = Noneable(StringValidator(multiline=True)), Default(None)
    address: AddressInput = DataclassValidator(AddressInput)
    shortcode: str = StringValidator()
    lat: float = FloatValidator(min_value=-90.0, max_value=90.0)
    lon: float = FloatValidator(min_value=-180.0, max_value=180.0)
    status: LocationStatus = EnumValidator(LocationStatus)
    published: bool = BooleanValidator()
    accessibilityType: AccessibilityType = EnumValidator(AccessibilityType)
    hours: Hours = DataclassValidator(Hours)
    operatorName: str = StringValidator()


@validataclass
class OperatorInput:
    placesCount: int = IntegerValidator()
    operatorId: str = IntegerValidator()
    operatorName: str = StringValidator()
    amountStations: int = IntegerValidator()
    amountIdentifications: int = IntegerValidator()
    amountUsers: int = IntegerValidator()
    # just check if it's a dict, validating single locations will be done on dataset level in order to catch exceptions on dataset level
    operatorPlaces: list[dict] = ListValidator(AnythingValidator(allowed_types=dict))


@validataclass
class LichtblickInput:
    operator: OperatorInput = DataclassValidator(OperatorInput)
