"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .day_week_month_extended_output import DayWeekMonthExtendedOutput


@dataclass(kw_only=True)
class DayWeekMonthExtensionTypeGOutput:
    DayWeekMonthExtended: DayWeekMonthExtendedOutput | None = None
