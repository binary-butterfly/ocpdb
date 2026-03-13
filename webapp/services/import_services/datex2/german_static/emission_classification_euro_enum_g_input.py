"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator

from .emission_classification_euro_enum import EmissionClassificationEuroEnum
from .emission_classification_euro_enum_extension_type_g import EmissionClassificationEuroEnumExtensionTypeG


@validataclass
class EmissionClassificationEuroEnumGInput:
    value: EmissionClassificationEuroEnum = EnumValidator(EmissionClassificationEuroEnum)
    extendedValueG: EmissionClassificationEuroEnumExtensionTypeG | UnsetValueType = (
        EnumValidator(EmissionClassificationEuroEnumExtensionTypeG),
        Default(UnsetValue),
    )
