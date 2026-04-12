"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .calendar_week_within_month_enum import CalendarWeekWithinMonthEnum


@dataclass(kw_only=True)
class CalendarWeekWithinMonthEnumGOutput:
    value: CalendarWeekWithinMonthEnum
    extendedValueG: str | None = None
