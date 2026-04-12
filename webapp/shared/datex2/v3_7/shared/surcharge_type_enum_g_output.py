"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .surcharge_type_enum import SurchargeTypeEnum


@dataclass(kw_only=True)
class SurchargeTypeEnumGOutput:
    value: SurchargeTypeEnum
    extendedValueG: str | None = None
