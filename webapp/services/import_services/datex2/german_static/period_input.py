"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator, StringValidator

from .day_week_month_g_input import DayWeekMonthGInput
from .extension_type_g_input import ExtensionTypeGInput
from .multilingual_string_input import MultilingualStringInput
from .special_day_g_input import SpecialDayGInput
from .time_period_of_day_input import TimePeriodOfDayInput


@validataclass
class PeriodInput:
    startOfPeriod: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    endOfPeriod: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    periodName: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    recurringTimePeriodOfDay: list[TimePeriodOfDayInput] | UnsetValueType = (
        ListValidator(DataclassValidator(TimePeriodOfDayInput)),
        Default(UnsetValue),
    )
    recurringDayWeekMonthPeriod: list[DayWeekMonthGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(DayWeekMonthGInput)),
        Default(UnsetValue),
    )
    recurringSpecialDay: list[SpecialDayGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(SpecialDayGInput)),
        Default(UnsetValue),
    )
    comPeriodExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
