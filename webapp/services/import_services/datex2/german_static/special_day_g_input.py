"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .public_holiday_input import PublicHolidayInput
from .special_day_input import SpecialDayInput


@validataclass
class SpecialDayGInput:
    comSpecialDay: SpecialDayInput | UnsetValueType = DataclassValidator(SpecialDayInput), Default(UnsetValue)
    comPublicHoliday: PublicHolidayInput | UnsetValueType = DataclassValidator(PublicHolidayInput), Default(UnsetValue)
