"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator, StringValidator

from webapp.shared.datex2.v3_7.shared.axle_spacing_input import AxleSpacingInput
from webapp.shared.datex2.v3_7.shared.axle_weight_input import AxleWeightInput
from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.hazardous_materials_g_input import HazardousMaterialsGInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput
from webapp.shared.datex2.v3_7.shared.vehicle_status_enum_g_input import VehicleStatusEnumGInput

from .vehicle_characteristics_input import VehicleCharacteristicsInput


@validataclass
class VehicleInput(ValidataclassMixin):
    anonymizedVehicleReference: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    vehicleColour: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    vehicleCountryOfOrigin: str | UnsetValueType = StringValidator(max_length=2), Default(UnsetValue)
    vehicleIdentifier: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    vehicleManufacturer: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    vehicleModel: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    vehicleRegistrationPlateIdentifier: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    vehicleStatus: VehicleStatusEnumGInput | UnsetValueType = (
        DataclassValidator(VehicleStatusEnumGInput),
        Default(UnsetValue),
    )
    vehicleCharacteristics: VehicleCharacteristicsInput | UnsetValueType = (
        DataclassValidator(VehicleCharacteristicsInput),
        Default(UnsetValue),
    )
    axleSpacingOnVehicle: list[AxleSpacingInput] | UnsetValueType = (
        ListValidator(DataclassValidator(AxleSpacingInput)),
        Default(UnsetValue),
    )
    specificAxleWeight: list[AxleWeightInput] | UnsetValueType = (
        ListValidator(DataclassValidator(AxleWeightInput)),
        Default(UnsetValue),
    )
    hazardousGoodsAssociatedWithVehicle: HazardousMaterialsGInput | UnsetValueType = (
        DataclassValidator(HazardousMaterialsGInput),
        Default(UnsetValue),
    )
    comVehicleExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
