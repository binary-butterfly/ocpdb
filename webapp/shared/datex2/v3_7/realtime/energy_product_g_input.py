"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .electric_energy_input import ElectricEnergyInput
from .energy_product_input import EnergyProductInput


@validataclass
class EnergyProductGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    aegiEnergyProduct: EnergyProductInput | UnsetValueType = DataclassValidator(EnergyProductInput), Default(UnsetValue)
    aegiElectricEnergy: ElectricEnergyInput | UnsetValueType = (
        DataclassValidator(ElectricEnergyInput),
        Default(UnsetValue),
    )
