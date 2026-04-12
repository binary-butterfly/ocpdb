"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .applicable_days_within_month_enum import ApplicableDaysWithinMonthEnum


@dataclass(kw_only=True)
class ApplicableDaysWithinMonthEnumGOutput:
    value: ApplicableDaysWithinMonthEnum
    extendedValueG: str | None = None
