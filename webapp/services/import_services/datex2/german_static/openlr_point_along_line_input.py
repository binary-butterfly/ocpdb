"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .extension_type_g_input import ExtensionTypeGInput
from .openlr_last_location_reference_point_input import OpenlrLastLocationReferencePointInput
from .openlr_location_reference_point_input import OpenlrLocationReferencePointInput
from .openlr_offsets_input import OpenlrOffsetsInput
from .openlr_orientation_enum_g_input import OpenlrOrientationEnumGInput
from .openlr_side_of_road_enum_g_input import OpenlrSideOfRoadEnumGInput


@validataclass
class OpenlrPointAlongLineInput:
    openlrSideOfRoad: OpenlrSideOfRoadEnumGInput = DataclassValidator(OpenlrSideOfRoadEnumGInput)
    openlrOrientation: OpenlrOrientationEnumGInput = DataclassValidator(OpenlrOrientationEnumGInput)
    openlrLocationReferencePoint: OpenlrLocationReferencePointInput = DataclassValidator(
        OpenlrLocationReferencePointInput
    )
    openlrLastLocationReferencePoint: OpenlrLastLocationReferencePointInput = DataclassValidator(
        OpenlrLastLocationReferencePointInput
    )
    openlrOffsets: OpenlrOffsetsInput | UnsetValueType = DataclassValidator(OpenlrOffsetsInput), Default(UnsetValue)
    locOpenlrPointLocationReferenceExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    locOpenlrBasePointLocationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    locOpenlrPointAlongLineExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
