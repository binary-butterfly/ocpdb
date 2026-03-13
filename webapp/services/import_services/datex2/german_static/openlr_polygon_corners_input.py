"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator

from .extension_type_g_input import ExtensionTypeGInput
from .point_coordinates_input import PointCoordinatesInput


@validataclass
class OpenlrPolygonCornersInput:
    openlrCoordinates: list[PointCoordinatesInput] = ListValidator(DataclassValidator(PointCoordinatesInput))
    locOpenlrPolygonCornersExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
