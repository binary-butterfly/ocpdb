"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, IntegerValidator

from .extension_type_g_input import ExtensionTypeGInput
from .point_coordinates_input import PointCoordinatesInput


@validataclass
class PointByCoordinatesInput:
    bearing: int | UnsetValueType = IntegerValidator(min_value=0.0), Default(UnsetValue)
    pointCoordinates: PointCoordinatesInput = DataclassValidator(PointCoordinatesInput)
    locPointByCoordinatesExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
