"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .engine_type_enum import EngineTypeEnum


@dataclass(kw_only=True)
class EngineTypeEnumGOutput:
    value: EngineTypeEnum
    extendedValueG: str | None = None
