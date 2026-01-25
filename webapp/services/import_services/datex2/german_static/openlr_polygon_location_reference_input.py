"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .extension_type_g_input import ExtensionTypeGInput
from .openlr_polygon_corners_input import OpenlrPolygonCornersInput


@validataclass
class OpenlrPolygonLocationReferenceInput:
    openlrPolygonCorners: OpenlrPolygonCornersInput = DataclassValidator(OpenlrPolygonCornersInput)
    locOpenlrAreaLocationReferenceExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    locOpenlrPolygonLocationReferenceExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
