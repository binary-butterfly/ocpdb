"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator

from .extension_type_g_input import ExtensionTypeGInput


@validataclass
class AmenitiesInput:
    illuminated: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    roofed: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    illuminatedRechargingParkingNearby: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    roofedRechargingParkingNearby: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    afacAmenitiesExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
