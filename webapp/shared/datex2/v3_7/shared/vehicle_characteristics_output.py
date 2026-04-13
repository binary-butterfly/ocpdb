"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .emissions_output import EmissionsOutput
from .fuel_type_enum_g_output import FuelTypeEnumGOutput
from .gross_weight_characteristic_output import GrossWeightCharacteristicOutput
from .heaviest_axle_weight_characteristic_output import HeaviestAxleWeightCharacteristicOutput
from .height_characteristic_output import HeightCharacteristicOutput
from .length_characteristic_output import LengthCharacteristicOutput
from .load_type_enum_g_output import LoadTypeEnumGOutput
from .number_of_axles_characteristic_output import NumberOfAxlesCharacteristicOutput
from .vehicle_characteristics_extension_type_g_output import VehicleCharacteristicsExtensionTypeGOutput
from .vehicle_equipment_enum_g_output import VehicleEquipmentEnumGOutput
from .vehicle_type_enum_g_output import VehicleTypeEnumGOutput
from .vehicle_usage_enum_g_output import VehicleUsageEnumGOutput
from .width_characteristic_output import WidthCharacteristicOutput


@dataclass(kw_only=True)
class VehicleCharacteristicsOutput:
    fuelType: list[FuelTypeEnumGOutput] | None = None
    loadType: LoadTypeEnumGOutput | None = None
    vehicleEquipment: VehicleEquipmentEnumGOutput | None = None
    vehicleType: list[VehicleTypeEnumGOutput] | None = None
    vehicleUsage: VehicleUsageEnumGOutput | None = None
    yearOfFirstRegistration: int | None = None
    grossWeightCharacteristic: list[GrossWeightCharacteristicOutput] | None = None
    heightCharacteristic: list[HeightCharacteristicOutput] | None = None
    lengthCharacteristic: list[LengthCharacteristicOutput] | None = None
    widthCharacteristic: list[WidthCharacteristicOutput] | None = None
    heaviestAxleWeightCharacteristic: list[HeaviestAxleWeightCharacteristicOutput] | None = None
    numberOfAxlesCharacteristic: list[NumberOfAxlesCharacteristicOutput] | None = None
    emissions: EmissionsOutput | None = None
    comVehicleCharacteristicsExtensionG: VehicleCharacteristicsExtensionTypeGOutput | None = None
