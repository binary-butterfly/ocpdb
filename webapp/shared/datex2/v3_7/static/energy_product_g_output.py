"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .electric_energy_output import ElectricEnergyOutput
from .energy_product_output import EnergyProductOutput


@dataclass(kw_only=True)
class EnergyProductGOutput:
    """
    Only one of the properties shall be used in an instance.
    """

    aegiEnergyProduct: EnergyProductOutput | None = None
    aegiElectricEnergy: ElectricEnergyOutput | None = None
