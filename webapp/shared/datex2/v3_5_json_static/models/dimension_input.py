"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, FloatValidator, IntegerValidator

from .extension_type_g_input import ExtensionTypeGInput


@validataclass
class DimensionInput(ValidataclassMixin):
    """
    A component that provides dimension information. Especially for multi-storey buildings, the usable area might be larger than the product from its length and width.
    """

    length: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    width: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    height: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    usableArea: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    afacDimensionExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
