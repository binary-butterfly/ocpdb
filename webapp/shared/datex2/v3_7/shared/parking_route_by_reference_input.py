"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .extension_type_g_input import ExtensionTypeGInput
from .parking_route_details_versioned_reference_g_input import ParkingRouteDetailsVersionedReferenceGInput
from .rgb_colour_input import RgbColourInput


@validataclass
class ParkingRouteByReferenceInput(ValidataclassMixin):
    parkingRouteReference: ParkingRouteDetailsVersionedReferenceGInput = DataclassValidator(
        ParkingRouteDetailsVersionedReferenceGInput
    )
    parkingRouteColour: RgbColourInput | UnsetValueType = DataclassValidator(RgbColourInput), Default(UnsetValue)
    prkParkingRouteExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    prkParkingRouteByReferenceExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
