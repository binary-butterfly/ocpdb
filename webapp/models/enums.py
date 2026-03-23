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
