"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .openlr_circle_location_reference_input import OpenlrCircleLocationReferenceInput
from .openlr_closed_line_location_reference_input import OpenlrClosedLineLocationReferenceInput
from .openlr_grid_location_reference_input import OpenlrGridLocationReferenceInput
from .openlr_polygon_location_reference_input import OpenlrPolygonLocationReferenceInput
from .openlr_rectangle_location_reference_input import OpenlrRectangleLocationReferenceInput


@validataclass
class OpenlrAreaLocationReferenceGInput:
    locOpenlrGridLocationReference: OpenlrGridLocationReferenceInput | UnsetValueType = (
        DataclassValidator(OpenlrGridLocationReferenceInput),
        Default(UnsetValue),
    )
    locOpenlrCircleLocationReference: OpenlrCircleLocationReferenceInput | UnsetValueType = (
        DataclassValidator(OpenlrCircleLocationReferenceInput),
        Default(UnsetValue),
    )
    locOpenlrClosedLineLocationReference: OpenlrClosedLineLocationReferenceInput | UnsetValueType = (
        DataclassValidator(OpenlrClosedLineLocationReferenceInput),
        Default(UnsetValue),
    )
    locOpenlrRectangleLocationReference: OpenlrRectangleLocationReferenceInput | UnsetValueType = (
        DataclassValidator(OpenlrRectangleLocationReferenceInput),
        Default(UnsetValue),
    )
    locOpenlrPolygonLocationReference: OpenlrPolygonLocationReferenceInput | UnsetValueType = (
        DataclassValidator(OpenlrPolygonLocationReferenceInput),
        Default(UnsetValue),
    )
