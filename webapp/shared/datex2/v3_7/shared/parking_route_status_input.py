"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator, ListValidator

from .extension_type_g_input import ExtensionTypeGInput
from .parking_route_details_versioned_reference_g_input import ParkingRouteDetailsVersionedReferenceGInput
from .travel_time_data_input import TravelTimeDataInput


@validataclass
class ParkingRouteStatusInput(ValidataclassMixin):
    parkingRouteReference: ParkingRouteDetailsVersionedReferenceGInput = DataclassValidator(
        ParkingRouteDetailsVersionedReferenceGInput
    )
    parkingRouteActive: bool = BooleanValidator()
    travelTimeData: list[TravelTimeDataInput] | UnsetValueType = (
        ListValidator(DataclassValidator(TravelTimeDataInput)),
        Default(UnsetValue),
    )
    prkParkingRouteStatusExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
