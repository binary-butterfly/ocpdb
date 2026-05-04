"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator

from .duration_value_input import DurationValueInput
from .extension_type_g_input import ExtensionTypeGInput
from .measurement_or_calculation_time_input import MeasurementOrCalculationTimeInput
from .speed_value_input import SpeedValueInput
from .travel_time_trend_type_enum_g_input import TravelTimeTrendTypeEnumGInput
from .travel_time_type_enum_g_input import TravelTimeTypeEnumGInput
from .vehicle_type_enum_g_input import VehicleTypeEnumGInput


@validataclass
class TravelTimeDataInput(ValidataclassMixin):
    travelTimeTrendType: TravelTimeTrendTypeEnumGInput | UnsetValueType = (
        DataclassValidator(TravelTimeTrendTypeEnumGInput),
        Default(UnsetValue),
    )
    travelTimeType: TravelTimeTypeEnumGInput | UnsetValueType = (
        DataclassValidator(TravelTimeTypeEnumGInput),
        Default(UnsetValue),
    )
    vehicleType: list[VehicleTypeEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(VehicleTypeEnumGInput)),
        Default(UnsetValue),
    )
    measurementOrCalculationTime: MeasurementOrCalculationTimeInput | UnsetValueType = (
        DataclassValidator(MeasurementOrCalculationTimeInput),
        Default(UnsetValue),
    )
    travelTime: DurationValueInput | UnsetValueType = DataclassValidator(DurationValueInput), Default(UnsetValue)
    freeFlowTravelTime: DurationValueInput | UnsetValueType = (
        DataclassValidator(DurationValueInput),
        Default(UnsetValue),
    )
    normallyExpectedTravelTime: DurationValueInput | UnsetValueType = (
        DataclassValidator(DurationValueInput),
        Default(UnsetValue),
    )
    travelTimeDelay: DurationValueInput | UnsetValueType = DataclassValidator(DurationValueInput), Default(UnsetValue)
    freeFlowSpeed: SpeedValueInput | UnsetValueType = DataclassValidator(SpeedValueInput), Default(UnsetValue)
    roaBasicDataExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    roaTravelTimeDataExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
