"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, FloatValidator

from .altitude_confidence_input import AltitudeConfidenceInput
from .extension_type_g_input import ExtensionTypeGInput
from .height_type_enum_g_input import HeightTypeEnumGInput
from .position_accuracy_input import PositionAccuracyInput


@validataclass
class HeightCoordinateInput:
    heightValue: int = FloatValidator()
    heightType: HeightTypeEnumGInput | UnsetValueType = DataclassValidator(HeightTypeEnumGInput), Default(UnsetValue)
    altitudeConfidence: AltitudeConfidenceInput | UnsetValueType = (
        DataclassValidator(AltitudeConfidenceInput),
        Default(UnsetValue),
    )
    verticalPositionAccuracy: PositionAccuracyInput | UnsetValueType = (
        DataclassValidator(PositionAccuracyInput),
        Default(UnsetValue),
    )
    locHeightCoordinateExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
