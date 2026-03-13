"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator

from .day_enum_g_input import DayEnumGInput
from .extension_type_g_input import ExtensionTypeGInput
from .month_of_year_enum_g_input import MonthOfYearEnumGInput


@validataclass
class DayWeekMonthInput:
    applicableDay: list[DayEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(DayEnumGInput)),
        Default(UnsetValue),
    )
    applicableMonth: list[MonthOfYearEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(MonthOfYearEnumGInput)),
        Default(UnsetValue),
    )
    comDayWeekMonthExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
