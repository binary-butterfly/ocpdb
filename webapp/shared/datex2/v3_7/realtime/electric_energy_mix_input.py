"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import (
    BooleanValidator,
    DataclassValidator,
    FloatValidator,
    IntegerValidator,
    ListValidator,
)

from webapp.shared.datex2.v3_7.shared.electric_energy_source_ratio_input import ElectricEnergySourceRatioInput
from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput

from .organisation_g_input import OrganisationGInput
from .rates_g_input import RatesGInput


@validataclass
class ElectricEnergyMixInput(ValidataclassMixin):
    energyMixIndex: int = IntegerValidator()
    energyProductName: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    isGreenEnergy: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    carbonDioxideImpact: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    nuclearWasteImpact: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    notAvailable: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
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
