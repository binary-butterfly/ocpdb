"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .direction_enum_g_input import DirectionEnumGInput
from .distance_along_linear_element_g_input import DistanceAlongLinearElementGInput
from .extension_type_g_input import ExtensionTypeGInput
from .height_grade_enum_g_input import HeightGradeEnumGInput
from .linear_direction_enum_g_input import LinearDirectionEnumGInput
from .linear_element_g_input import LinearElementGInput
from .multilingual_string_input import MultilingualStringInput


@validataclass
class PointAlongLinearElementInput(ValidataclassMixin):
    administrativeAreaOfPoint: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    directionAtPoint: DirectionEnumGInput | UnsetValueType = (
        DataclassValidator(DirectionEnumGInput),
        Default(UnsetValue),
    )
    directionRelativeAtPoint: LinearDirectionEnumGInput | UnsetValueType = (
        DataclassValidator(LinearDirectionEnumGInput),
        Default(UnsetValue),
    )
    heightGradeOfPoint: HeightGradeEnumGInput | UnsetValueType = (
        DataclassValidator(HeightGradeEnumGInput),
        Default(UnsetValue),
    )
    linearElement: LinearElementGInput = DataclassValidator(LinearElementGInput)
    distanceAlongLinearElement: DistanceAlongLinearElementGInput = DataclassValidator(DistanceAlongLinearElementGInput)
    locPointAlongLinearElementExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
