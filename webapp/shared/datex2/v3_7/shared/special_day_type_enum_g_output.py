"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .special_day_type_enum import SpecialDayTypeEnum


@dataclass(kw_only=True)
class SpecialDayTypeEnumGOutput:
    value: SpecialDayTypeEnum
    extendedValueG: str | None = None
