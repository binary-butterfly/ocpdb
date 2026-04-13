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

from enum import Enum

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.validators import BooleanValidator, EnumValidator, IntegerValidator, ListValidator, Noneable


class ChargingRateUnit(Enum):
    W = 'W'
    KW = 'KW'
    A = 'A'


class TariffType(Enum):
    AD_HOC_PAYMENT = 'AD_HOC_PAYMENT'
    PROFILE_CHEAP = 'PROFILE_CHEAP'
    PROFILE_FAST = 'PROFILE_FAST'
    PROFILE_GREEN = 'PROFILE_GREEN'
    REGULAR = 'REGULAR'


class TariffAudience(Enum):
    AD_HOC_PAYMENT = 'AD_HOC_PAYMENT'
    EMSP_CONTRACT = 'EMSP_CONTRACT'


class TariffDimensionType(Enum):
    ENERGY = 'ENERGY'
    TIME = 'TIME'
    FLAT = 'FLAT'
    PARKING_TIME = 'PARKING_TIME'


class DayOfWeek(Enum):
    MONDAY = 'MONDAY'
    TUESDAY = 'TUESDAY'
    WEDNESDAY = 'WEDNESDAY'
    THURSDAY = 'THURSDAY'
    FRIDAY = 'FRIDAY'
    SATURDAY = 'SATURDAY'
    SUNDAY = 'SUNDAY'


class ReservationRestrictionType:
    RESERVATION = 'RESERVATION'
    RESERVATION_EXPIRES = 'RESERVATION_EXPIRES'


class VehicleCategoryEnum(Enum):
    L1 = 'l1'
    L2 = 'l2'
    L3 = 'l3'
    L4 = 'l4'
    L5 = 'l5'
    L6 = 'l6'
    L7 = 'l7'
    M = 'm'
    R = 'r'
    R1 = 'r1'
    R2 = 'r2'
    R3 = 'r3'
    R4 = 'r4'
    T1 = 't1'
    T2 = 't2'
    T3 = 't3'
    T4 = 't4'
    T41 = 't41'
    T42 = 't42'
    T43 = 't43'
    M1 = 'm1'
    M2 = 'm2'
    M3 = 'm3'
    N = 'n'
    N1 = 'n1'
    N2 = 'n2'
    N3 = 'n3'
    O = 'o'  # noqa: E741
    O1 = 'o1'
    O2 = 'o2'
    O3 = 'o3'
    O4 = 'o4'


@validataclass
class ParkingSpace(ValidataclassMixin):
    vehicle_types: list[VehicleCategoryEnum] = ListValidator(EnumValidator(VehicleCategoryEnum))
    parking_space_count: int = IntegerValidator(min_value=0)
    max_weight: int | None = Noneable(IntegerValidator(min_value=1)), Default(None)  # in kg
    max_height: int | None = Noneable(IntegerValidator(min_value=1)), Default(None)  # in cm
    max_length: int | None = Noneable(IntegerValidator(min_value=1)), Default(None)  # in cm
    max_width: int | None = Noneable(IntegerValidator(min_value=1)), Default(None)  # in cm
    has_roof: bool = BooleanValidator(), Default(False)
    is_illuminated: bool = BooleanValidator(), Default(False)
    is_accessible: bool = BooleanValidator(), Default(False)
