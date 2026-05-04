"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, FloatValidator

from .extension_type_g_input import ExtensionTypeGInput
from .mobility_type_enum_g_input import MobilityTypeEnumGInput


@validataclass
class MobilityInput(ValidataclassMixin):
    mobilityType: MobilityTypeEnumGInput = DataclassValidator(MobilityTypeEnumGInput)
    speed: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    sitMobilityExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
