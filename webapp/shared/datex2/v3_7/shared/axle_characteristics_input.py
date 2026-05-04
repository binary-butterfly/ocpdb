"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, FloatValidator

from .extension_type_g_input import ExtensionTypeGInput


@validataclass
class AxleCharacteristicsInput(ValidataclassMixin):
    maximumWeight: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    minimumWeight: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    roaAxleCharacteristicsExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
