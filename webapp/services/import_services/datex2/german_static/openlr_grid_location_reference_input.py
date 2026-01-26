"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, IntegerValidator

from .extension_type_g_input import ExtensionTypeGInput
from .openlr_rectangle_input import OpenlrRectangleInput


@validataclass
class OpenlrGridLocationReferenceInput:
    openlrNumColumns: int = IntegerValidator(min_value=0)
    openlrNumRows: int = IntegerValidator(min_value=0)
    openlrRectangle: OpenlrRectangleInput = DataclassValidator(OpenlrRectangleInput)
    locOpenlrAreaLocationReferenceExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    locOpenlrGridLocationReferenceExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
