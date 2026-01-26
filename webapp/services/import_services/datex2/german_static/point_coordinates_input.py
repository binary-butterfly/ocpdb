"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from decimal import Decimal

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator, NumericValidator

from .extension_type_g_input import ExtensionTypeGInput
from .height_coordinate_input import HeightCoordinateInput
from .position_accuracy_input import PositionAccuracyInput
from .position_confidence_ellipse_input import PositionConfidenceEllipseInput


@validataclass
class PointCoordinatesInput:
    latitude: Decimal = NumericValidator()
    longitude: Decimal = NumericValidator()
    heightCoordinate: list[HeightCoordinateInput] | UnsetValueType = (
        ListValidator(DataclassValidator(HeightCoordinateInput)),
        Default(UnsetValue),
    )
    positionConfidenceEllipse: PositionConfidenceEllipseInput | UnsetValueType = (
        DataclassValidator(PositionConfidenceEllipseInput),
        Default(UnsetValue),
    )
    horizontalPositionAccuracy: PositionAccuracyInput | UnsetValueType = (
        DataclassValidator(PositionAccuracyInput),
        Default(UnsetValue),
    )
    locPointCoordinatesExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
