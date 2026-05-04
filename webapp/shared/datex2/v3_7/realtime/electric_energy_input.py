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
    ListValidator,
    StringValidator,
)

from webapp.shared.datex2.v3_7.shared.electric_energy_source_ratio_input import ElectricEnergySourceRatioInput
from webapp.shared.datex2.v3_7.shared.energy_rate_input import EnergyRateInput
from webapp.shared.datex2.v3_7.shared.energy_rate_reference_g_input import EnergyRateReferenceGInput
from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput

from .organisation_g_input import OrganisationGInput


@validataclass
class ElectricEnergyInput(ValidataclassMixin):
    energyProductName: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    isGreenEnergy: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    energyRateByReference: list[EnergyRateReferenceGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(EnergyRateReferenceGInput)),
        Default(UnsetValue),
    )
    energyProductInformation: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    renewableEnergyEvidence: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    carbonDioxideImpact: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    nuclearWasteImpact: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    mobilityServiceProvider: list[OrganisationGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(OrganisationGInput)),
        Default(UnsetValue),
    )
    energyRate: list[EnergyRateInput] | UnsetValueType = (
        ListValidator(DataclassValidator(EnergyRateInput)),
        Default(UnsetValue),
    )
    electricEnergySourceRatio: list[ElectricEnergySourceRatioInput] | UnsetValueType = (
        ListValidator(DataclassValidator(ElectricEnergySourceRatioInput)),
        Default(UnsetValue),
    )
    aegiEnergyProductExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    aegiElectricEnergyExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
