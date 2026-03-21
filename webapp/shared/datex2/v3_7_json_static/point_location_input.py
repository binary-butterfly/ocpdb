"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .extension_type_g_input import ExtensionTypeGInput
from .location_reference_extension_type_g_input import LocationReferenceExtensionTypeGInput
from .point_by_coordinates_input import PointByCoordinatesInput


@validataclass
class PointLocationInput(ValidataclassMixin):
    """
    Location representing a single geospatial point.
    """

    pointByCoordinates: PointByCoordinatesInput | UnsetValueType = (
        DataclassValidator(PointByCoordinatesInput),
        Default(UnsetValue),
    )
    locLocationReferenceExtensionG: LocationReferenceExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(LocationReferenceExtensionTypeGInput),
        Default(UnsetValue),
    )
    locLocationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    locNetworkLocationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    locPointLocationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
