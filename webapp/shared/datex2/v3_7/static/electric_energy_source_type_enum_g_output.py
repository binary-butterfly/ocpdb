"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .electric_energy_source_type_enum import ElectricEnergySourceTypeEnum


@dataclass(kw_only=True)
class ElectricEnergySourceTypeEnumGOutput:
    value: ElectricEnergySourceTypeEnum
    extendedValueG: str | None = None
