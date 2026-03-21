"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator, StringValidator

from .day_week_month_g_input import DayWeekMonthGInput
from .multilingual_string_input import MultilingualStringInput
from .period_extension_type_g_input import PeriodExtensionTypeGInput
from .special_day_g_input import SpecialDayGInput
from .time_period_of_day_input import TimePeriodOfDayInput


@validataclass
class PeriodInput(ValidataclassMixin):
    """
    A continuous time period or a set of discontinuous time periods defined by the intersection of a set of criteria all within an overall delimiting interval.
    """

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
    comPeriodExtensionG: PeriodExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(PeriodExtensionTypeGInput),
        Default(UnsetValue),
    )
