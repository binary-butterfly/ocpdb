"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator, ListValidator, StringValidator

from webapp.shared.datex2.v3_7.shared.direction_enum_g_input import DirectionEnumGInput
from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput
from webapp.shared.datex2.v3_7.shared.parking_route_orientation_enum_g_input import ParkingRouteOrientationEnumGInput
from webapp.shared.datex2.v3_7.shared.parking_route_type_enum_g_input import ParkingRouteTypeEnumGInput
from webapp.shared.datex2.v3_7.shared.rgb_colour_input import RgbColourInput

from .location_reference_g_input import LocationReferenceGInput
from .parking_vms_input import ParkingVmsInput


@validataclass
class ParkingRouteDetailsInput(ValidataclassMixin):
    idG: str = StringValidator()
    versionG: str = StringValidator()
    name: MultilingualStringInput | UnsetValueType = DataclassValidator(MultilingualStringInput), Default(UnsetValue)
    type: ParkingRouteTypeEnumGInput | UnsetValueType = (
        DataclassValidator(ParkingRouteTypeEnumGInput),
        Default(UnsetValue),
    )
    dynamicRouteManagement: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    iconIndex: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    direction: DirectionEnumGInput | UnsetValueType = DataclassValidator(DirectionEnumGInput), Default(UnsetValue)
    orientation: list[ParkingRouteOrientationEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(ParkingRouteOrientationEnumGInput)),
        Default(UnsetValue),
    )
    parkingRouteColour: RgbColourInput | UnsetValueType = DataclassValidator(RgbColourInput), Default(UnsetValue)
    locationReference: LocationReferenceGInput | UnsetValueType = (
        DataclassValidator(LocationReferenceGInput),
        Default(UnsetValue),
    )
    parkingVms: list[ParkingVmsInput] | UnsetValueType = (
        ListValidator(DataclassValidator(ParkingVmsInput)),
        Default(UnsetValue),
    )
    prkParkingRouteExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    prkParkingRouteDetailsExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
