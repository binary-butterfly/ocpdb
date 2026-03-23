"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator, StringValidator

from .energy_price_input import EnergyPriceInput
from .energy_rate_reference_g_input import EnergyRateReferenceGInput
from .extension_type_g_input import ExtensionTypeGInput
from .multilingual_string_input import MultilingualStringInput


@validataclass
class EnergyRateUpdateInput(ValidataclassMixin):
    """
    Updates a rate defined in the static part of the model.
    """

    lastUpdated: str = StringValidator()
    energyRateReference: EnergyRateReferenceGInput = DataclassValidator(EnergyRateReferenceGInput)
    additionalInformation: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    energyPrice: list[EnergyPriceInput] | UnsetValueType = (
        ListValidator(DataclassValidator(EnergyPriceInput)),
        Default(UnsetValue),
    )
    aegiEnergyRateUpdateExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
