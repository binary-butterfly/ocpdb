"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator

from .calendar_week_within_month_enum_g_input import CalendarWeekWithinMonthEnumGInput
from .day_enum_g_input import DayEnumGInput
from .day_week_month_extension_type_g_input import DayWeekMonthExtensionTypeGInput
from .extension_type_g_input import ExtensionTypeGInput
from .month_of_year_enum_g_input import MonthOfYearEnumGInput


@validataclass
class CalendarWeekWithinMonthInput(ValidataclassMixin):
    applicableDay: list[DayEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(DayEnumGInput)),
        Default(UnsetValue),
    )
    applicableMonth: list[MonthOfYearEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(MonthOfYearEnumGInput)),
        Default(UnsetValue),
    )
    applicableCalenderWeekWithinMonth: list[CalendarWeekWithinMonthEnumGInput] = ListValidator(
        DataclassValidator(CalendarWeekWithinMonthEnumGInput)
    )
    comDayWeekMonthExtensionG: DayWeekMonthExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(DayWeekMonthExtensionTypeGInput),
        Default(UnsetValue),
    )
    comCalendarWeekWithinMonthExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
