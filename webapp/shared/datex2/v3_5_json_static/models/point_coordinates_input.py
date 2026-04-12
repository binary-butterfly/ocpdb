"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, FloatValidator, ListValidator

from .extension_type_g_input import ExtensionTypeGInput
from .height_coordinate_input import HeightCoordinateInput
from .position_accuracy_input import PositionAccuracyInput
from .position_confidence_ellipse_input import PositionConfidenceEllipseInput


@validataclass
class PointCoordinatesInput(ValidataclassMixin):
    """
    A pair of planar coordinates defining the geodetic position of a single point using the European Terrestrial Reference System 1989 (ETRS89).
    """

    latitude: float = FloatValidator()
    longitude: float = FloatValidator()
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
