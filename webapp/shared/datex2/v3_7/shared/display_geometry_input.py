"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, FloatValidator, IntegerValidator

from .extension_type_g_input import ExtensionTypeGInput


@validataclass
class DisplayGeometryInput(ValidataclassMixin):
    pixelsAcross: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    pixelsDown: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    displayHeight: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    displayWidth: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    positionX: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    positionY: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    vmsDisplayGeometryExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
