"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .extension_type_g_input import ExtensionTypeGInput
from .openlr_last_location_reference_point_input import OpenlrLastLocationReferencePointInput
from .openlr_location_reference_point_input import OpenlrLocationReferencePointInput
from .openlr_offsets_input import OpenlrOffsetsInput
from .openlr_orientation_enum_g_input import OpenlrOrientationEnumGInput
from .openlr_side_of_road_enum_g_input import OpenlrSideOfRoadEnumGInput
from .point_coordinates_input import PointCoordinatesInput


@validataclass
class OpenlrPoiWithAccessPointInput(ValidataclassMixin):
    """
    A point of interest (POI) along a line with access is a point location which is defined by a linear reference path, an offset value (defining the access point) from the starting node of this path and a coordinate pair that defines the POI itself.
    """

    openlrSideOfRoad: OpenlrSideOfRoadEnumGInput = DataclassValidator(OpenlrSideOfRoadEnumGInput)
    openlrOrientation: OpenlrOrientationEnumGInput = DataclassValidator(OpenlrOrientationEnumGInput)
    openlrLocationReferencePoint: OpenlrLocationReferencePointInput = DataclassValidator(
        OpenlrLocationReferencePointInput
    )
    openlrLastLocationReferencePoint: OpenlrLastLocationReferencePointInput = DataclassValidator(
        OpenlrLastLocationReferencePointInput
    )
    openlrOffsets: OpenlrOffsetsInput | UnsetValueType = DataclassValidator(OpenlrOffsetsInput), Default(UnsetValue)
    openlrCoordinates: PointCoordinatesInput = DataclassValidator(PointCoordinatesInput)
    locOpenlrPointLocationReferenceExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    locOpenlrBasePointLocationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    locOpenlrPoiWithAccessPointExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
