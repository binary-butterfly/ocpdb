"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import (
    BooleanValidator,
    DataclassValidator,
    FloatValidator,
    ListValidator,
    StringValidator,
)

from .energy_rate_input import EnergyRateInput
from .energy_rate_reference_g_input import EnergyRateReferenceGInput
from .extension_type_g_input import ExtensionTypeGInput
from .multilingual_string_input import MultilingualStringInput
from .organisation_g_input import OrganisationGInput


@validataclass
class ElectricEnergyInput:
    energyProductName: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    isGreenEnergy: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    carbonDioxideImpact: int | UnsetValueType = FloatValidator(), Default(UnsetValue)
    nuclearWasteImpact: int | UnsetValueType = FloatValidator(), Default(UnsetValue)
    energyRateByReference: list[EnergyRateReferenceGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(EnergyRateReferenceGInput)),
        Default(UnsetValue),
    )
    energyProductInformation: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    renewableEnergyEvidence: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    mobilityServiceProvider: list[OrganisationGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(OrganisationGInput)),
        Default(UnsetValue),
    )
    energyRate: list[EnergyRateInput] | UnsetValueType = (
        ListValidator(DataclassValidator(EnergyRateInput)),
        Default(UnsetValue),
    )
    aegiElectricEnergyExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
