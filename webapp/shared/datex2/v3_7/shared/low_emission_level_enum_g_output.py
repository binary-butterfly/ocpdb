"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .low_emission_level_enum import LowEmissionLevelEnum


@dataclass(kw_only=True)
class LowEmissionLevelEnumGOutput:
    value: LowEmissionLevelEnum
    extendedValueG: str | None = None
