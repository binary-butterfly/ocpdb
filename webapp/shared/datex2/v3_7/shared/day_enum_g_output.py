"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .day_enum import DayEnum


@dataclass(kw_only=True)
class DayEnumGOutput:
    value: DayEnum
    extendedValueG: str | None = None
