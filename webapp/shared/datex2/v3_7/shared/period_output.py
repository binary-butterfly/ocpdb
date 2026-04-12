"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass
from datetime import datetime

from .day_week_month_g_output import DayWeekMonthGOutput
from .multilingual_string_output import MultilingualStringOutput
from .period_extension_type_g_output import PeriodExtensionTypeGOutput
from .special_day_g_output import SpecialDayGOutput
from .time_period_of_day_output import TimePeriodOfDayOutput


@dataclass(kw_only=True)
class PeriodOutput:
    startOfPeriod: datetime | None = None
    endOfPeriod: datetime | None = None
    periodName: MultilingualStringOutput | None = None
    recurringTimePeriodOfDay: list[TimePeriodOfDayOutput] | None = None
    recurringDayWeekMonthPeriod: list[DayWeekMonthGOutput] | None = None
    recurringSpecialDay: list[SpecialDayGOutput] | None = None
    comPeriodExtensionG: PeriodExtensionTypeGOutput | None = None
