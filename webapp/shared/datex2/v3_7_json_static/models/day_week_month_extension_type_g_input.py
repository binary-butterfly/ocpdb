"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .day_week_month_extended_input import DayWeekMonthExtendedInput


@validataclass
class DayWeekMonthExtensionTypeGInput(ValidataclassMixin):
    DayWeekMonthExtended: DayWeekMonthExtendedInput | UnsetValueType = (
        DataclassValidator(DayWeekMonthExtendedInput),
        Default(UnsetValue),
    )
