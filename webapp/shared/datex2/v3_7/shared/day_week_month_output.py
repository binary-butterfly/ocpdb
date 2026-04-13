"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .day_enum_g_output import DayEnumGOutput
from .day_week_month_extension_type_g_output import DayWeekMonthExtensionTypeGOutput
from .month_of_year_enum_g_output import MonthOfYearEnumGOutput


@dataclass(kw_only=True)
class DayWeekMonthOutput:
    applicableDay: list[DayEnumGOutput] | None = None
    applicableMonth: list[MonthOfYearEnumGOutput] | None = None
    comDayWeekMonthExtensionG: DayWeekMonthExtensionTypeGOutput | None = None
