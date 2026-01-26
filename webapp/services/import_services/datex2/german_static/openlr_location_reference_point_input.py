"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .extension_type_g_input import ExtensionTypeGInput
from .openlr_line_attributes_input import OpenlrLineAttributesInput
from .openlr_path_attributes_input import OpenlrPathAttributesInput
from .point_coordinates_input import PointCoordinatesInput


@validataclass
class OpenlrLocationReferencePointInput:
    openlrCoordinates: PointCoordinatesInput = DataclassValidator(PointCoordinatesInput)
    openlrLineAttributes: OpenlrLineAttributesInput = DataclassValidator(OpenlrLineAttributesInput)
    openlrPathAttributes: OpenlrPathAttributesInput = DataclassValidator(OpenlrPathAttributesInput)
    locOpenlrBaseReferencePointExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    locOpenlrLocationReferencePointExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
