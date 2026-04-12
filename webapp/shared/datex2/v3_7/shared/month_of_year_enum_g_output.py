"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .month_of_year_enum import MonthOfYearEnum


@dataclass(kw_only=True)
class MonthOfYearEnumGOutput:
    value: MonthOfYearEnum
    extendedValueG: str | None = None
