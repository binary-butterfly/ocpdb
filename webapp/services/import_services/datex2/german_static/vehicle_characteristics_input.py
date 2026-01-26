"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, IntegerValidator, ListValidator

from .emissions_input import EmissionsInput
from .fuel_type_enum_g_input import FuelTypeEnumGInput
from .gross_weight_characteristic_input import GrossWeightCharacteristicInput
from .heaviest_axle_weight_characteristic_input import HeaviestAxleWeightCharacteristicInput
from .height_characteristic_input import HeightCharacteristicInput
from .length_characteristic_input import LengthCharacteristicInput
from .load_type_enum_g_input import LoadTypeEnumGInput
from .number_of_axles_characteristic_input import NumberOfAxlesCharacteristicInput
from .vehicle_characteristics_extension_type_g_input import VehicleCharacteristicsExtensionTypeGInput
from .vehicle_equipment_enum_g_input import VehicleEquipmentEnumGInput
from .vehicle_type_enum_g_input import VehicleTypeEnumGInput
from .vehicle_usage_enum_g_input import VehicleUsageEnumGInput
from .width_characteristic_input import WidthCharacteristicInput


@validataclass
class VehicleCharacteristicsInput:
    fuelType: list[FuelTypeEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(FuelTypeEnumGInput)),
        Default(UnsetValue),
    )
    loadType: LoadTypeEnumGInput | UnsetValueType = DataclassValidator(LoadTypeEnumGInput), Default(UnsetValue)
    vehicleEquipment: VehicleEquipmentEnumGInput | UnsetValueType = (
        DataclassValidator(VehicleEquipmentEnumGInput),
        Default(UnsetValue),
    )
    vehicleType: list[VehicleTypeEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(VehicleTypeEnumGInput)),
        Default(UnsetValue),
    )
    vehicleUsage: VehicleUsageEnumGInput | UnsetValueType = (
        DataclassValidator(VehicleUsageEnumGInput),
        Default(UnsetValue),
    )
    yearOfFirstRegistration: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    grossWeightCharacteristic: list[GrossWeightCharacteristicInput] | UnsetValueType = (
        ListValidator(DataclassValidator(GrossWeightCharacteristicInput)),
        Default(UnsetValue),
    )
    heightCharacteristic: list[HeightCharacteristicInput] | UnsetValueType = (
        ListValidator(DataclassValidator(HeightCharacteristicInput)),
        Default(UnsetValue),
    )
    lengthCharacteristic: list[LengthCharacteristicInput] | UnsetValueType = (
        ListValidator(DataclassValidator(LengthCharacteristicInput)),
        Default(UnsetValue),
    )
    widthCharacteristic: list[WidthCharacteristicInput] | UnsetValueType = (
        ListValidator(DataclassValidator(WidthCharacteristicInput)),
        Default(UnsetValue),
    )
    heaviestAxleWeightCharacteristic: list[HeaviestAxleWeightCharacteristicInput] | UnsetValueType = (
        ListValidator(DataclassValidator(HeaviestAxleWeightCharacteristicInput)),
        Default(UnsetValue),
    )
    numberOfAxlesCharacteristic: list[NumberOfAxlesCharacteristicInput] | UnsetValueType = (
        ListValidator(DataclassValidator(NumberOfAxlesCharacteristicInput)),
        Default(UnsetValue),
    )
    emissions: EmissionsInput | UnsetValueType = DataclassValidator(EmissionsInput), Default(UnsetValue)
    comVehicleCharacteristicsExtensionG: VehicleCharacteristicsExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(VehicleCharacteristicsExtensionTypeGInput),
        Default(UnsetValue),
    )
