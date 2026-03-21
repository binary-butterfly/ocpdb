"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, FloatValidator

from .extension_type_g_input import ExtensionTypeGInput
from .height_type_enum_g_input import HeightTypeEnumGInput


@validataclass
class HeightCoordinateInput(ValidataclassMixin):
    """
    Third coordinate for points defined geodetically
    """

    heightValue: int = FloatValidator()
    heightType: HeightTypeEnumGInput | UnsetValueType = DataclassValidator(HeightTypeEnumGInput), Default(UnsetValue)
    locHeightCoordinateExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
