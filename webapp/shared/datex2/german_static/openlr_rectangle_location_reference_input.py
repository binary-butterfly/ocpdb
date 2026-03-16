"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .extension_type_g_input import ExtensionTypeGInput
from .openlr_rectangle_input import OpenlrRectangleInput


@validataclass
class OpenlrRectangleLocationReferenceInput(ValidataclassMixin):
    """
    The openLR method of area definition by providing a rectangular shape defined by two geo-coordinate pairs
    """

    openlrRectangle: OpenlrRectangleInput = DataclassValidator(OpenlrRectangleInput)
    locOpenlrAreaLocationReferenceExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    locOpenlrRectangleLocationReferenceExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
