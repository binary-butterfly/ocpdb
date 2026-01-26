"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator, StringValidator

from .emission_classification_euro_enum_g_input import EmissionClassificationEuroEnumGInput
from .emissions_extension_type_g_input import EmissionsExtensionTypeGInput
from .low_emission_level_enum_g_input import LowEmissionLevelEnumGInput


@validataclass
class EmissionsInput:
    emissionClassificationEuro: EmissionClassificationEuroEnumGInput | UnsetValueType = (
        DataclassValidator(EmissionClassificationEuroEnumGInput),
        Default(UnsetValue),
    )
    emissionClassificationOther: list[str] | UnsetValueType = ListValidator(StringValidator()), Default(UnsetValue)
    emissionLevel: LowEmissionLevelEnumGInput | UnsetValueType = (
        DataclassValidator(LowEmissionLevelEnumGInput),
        Default(UnsetValue),
    )
    comEmissionsExtensionG: EmissionsExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(EmissionsExtensionTypeGInput),
        Default(UnsetValue),
    )
