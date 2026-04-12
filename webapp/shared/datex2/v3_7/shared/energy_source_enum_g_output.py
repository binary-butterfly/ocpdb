"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .energy_source_enum import EnergySourceEnum


@dataclass(kw_only=True)
class EnergySourceEnumGOutput:
    value: EnergySourceEnum
    extendedValueG: str | None = None
