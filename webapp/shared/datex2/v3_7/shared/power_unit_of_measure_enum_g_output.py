"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .power_unit_of_measure_enum import PowerUnitOfMeasureEnum


@dataclass(kw_only=True)
class PowerUnitOfMeasureEnumGOutput:
    value: PowerUnitOfMeasureEnum
    extendedValueG: str | None = None
