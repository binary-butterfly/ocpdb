"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from webapp.shared.datex2.v3_7.shared.extension_type_g_output import ExtensionTypeGOutput

from .electric_energy_source_type_enum_g_output import ElectricEnergySourceTypeEnumGOutput
from .percentage_value_output import PercentageValueOutput


@dataclass(kw_only=True)
class ElectricEnergySourceRatioOutput:
    energySource: ElectricEnergySourceTypeEnumGOutput
    otherEnergySource: str | None = None
    sourceRatioValue: PercentageValueOutput
    aegiElectricEnergySourceRatioExtensionG: ExtensionTypeGOutput | None = None
