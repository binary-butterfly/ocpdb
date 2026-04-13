"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .nuts_code_type_enum import NutsCodeTypeEnum


@dataclass(kw_only=True)
class NutsCodeTypeEnumGOutput:
    value: NutsCodeTypeEnum
    extendedValueG: str | None = None
