"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .current_type_enum import CurrentTypeEnum


@dataclass(kw_only=True)
class CurrentTypeEnumGOutput:
    value: CurrentTypeEnum
    extendedValueG: str | None = None
