"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .calendar_week_within_month_output import CalendarWeekWithinMonthOutput
from .day_week_month_output import DayWeekMonthOutput
from .instance_of_day_within_month_output import InstanceOfDayWithinMonthOutput


@dataclass(kw_only=True)
class DayWeekMonthGOutput:
    """
    Only one of the properties shall be used in an instance.
    """

    comDayWeekMonth: DayWeekMonthOutput | None = None
    comInstanceOfDayWithinMonth: InstanceOfDayWithinMonthOutput | None = None
    comCalendarWeekWithinMonth: CalendarWeekWithinMonthOutput | None = None
