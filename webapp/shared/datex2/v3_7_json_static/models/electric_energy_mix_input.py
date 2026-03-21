"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator, IntegerValidator, ListValidator

from .electric_energy_source_ratio_input import ElectricEnergySourceRatioInput
from .extension_type_g_input import ExtensionTypeGInput
from .organisation_g_input import OrganisationGInput
from .rates_g_input import RatesGInput


@validataclass
class ElectricEnergyMixInput(ValidataclassMixin):
    """
    The energy mix and environmental impact of the supplied energy available at this charging point.
    """

    energyMixIndex: int = IntegerValidator()
    isGreenEnergy: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    electricEnergySourceRatio: list[ElectricEnergySourceRatioInput] | UnsetValueType = (
        ListValidator(DataclassValidator(ElectricEnergySourceRatioInput)),
        Default(UnsetValue),
    )
    energyProvider: OrganisationGInput | UnsetValueType = DataclassValidator(OrganisationGInput), Default(UnsetValue)
    rates: RatesGInput | UnsetValueType = DataclassValidator(RatesGInput), Default(UnsetValue)
    egiElectricEnergyMixExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
