"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .rate_line_usage_conditions_type_enum import RateLineUsageConditionsTypeEnum


@dataclass(kw_only=True)
class RateLineUsageConditionsTypeEnumGOutput:
    value: RateLineUsageConditionsTypeEnum
    extendedValueG: str | None = None
