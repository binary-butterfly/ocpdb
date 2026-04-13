"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .named_area_type_enum import NamedAreaTypeEnum


@dataclass(kw_only=True)
class NamedAreaTypeEnumGOutput:
    value: NamedAreaTypeEnum
    extendedValueG: str | None = None
