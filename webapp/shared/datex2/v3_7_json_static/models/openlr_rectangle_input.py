"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .extension_type_g_input import ExtensionTypeGInput
from .point_coordinates_input import PointCoordinatesInput


@validataclass
class OpenlrRectangleInput(ValidataclassMixin):
    """
    Area delimited by a rectangle defined by the geodetic co-ordinates of the two ends of its diagonal from south-west to north-east (the rectangle having two sides that are parallel to lines of latitude)
    """

    openlrLowerLeft: PointCoordinatesInput = DataclassValidator(PointCoordinatesInput)
    openlrUpperRight: PointCoordinatesInput = DataclassValidator(PointCoordinatesInput)
    locOpenlrRectangleExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
