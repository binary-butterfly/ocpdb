"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .calendar_week_within_month_input import CalendarWeekWithinMonthInput
from .day_week_month_input import DayWeekMonthInput
from .instance_of_day_within_month_input import InstanceOfDayWithinMonthInput


@validataclass
class DayWeekMonthGInput:
    comDayWeekMonth: DayWeekMonthInput | UnsetValueType = DataclassValidator(DayWeekMonthInput), Default(UnsetValue)
    comInstanceOfDayWithinMonth: InstanceOfDayWithinMonthInput | UnsetValueType = (
        DataclassValidator(InstanceOfDayWithinMonthInput),
        Default(UnsetValue),
    )
    comCalendarWeekWithinMonth: CalendarWeekWithinMonthInput | UnsetValueType = (
        DataclassValidator(CalendarWeekWithinMonthInput),
        Default(UnsetValue),
    )
