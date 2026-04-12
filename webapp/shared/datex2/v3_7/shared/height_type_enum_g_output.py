"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .height_type_enum import HeightTypeEnum


@dataclass(kw_only=True)
class HeightTypeEnumGOutput:
    value: HeightTypeEnum
    extendedValueG: str | None = None
