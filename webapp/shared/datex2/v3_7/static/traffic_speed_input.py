"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.measurement_or_calculation_time_input import MeasurementOrCalculationTimeInput
from webapp.shared.datex2.v3_7.shared.speed_percentile_input import SpeedPercentileInput
from webapp.shared.datex2.v3_7.shared.speed_value_input import SpeedValueInput

from .vehicle_characteristics_input import VehicleCharacteristicsInput


@validataclass
class TrafficSpeedInput(ValidataclassMixin):
    measurementOrCalculationTime: MeasurementOrCalculationTimeInput | UnsetValueType = (
        DataclassValidator(MeasurementOrCalculationTimeInput),
        Default(UnsetValue),
    )
    forVehiclesWithCharacteristicsOf: VehicleCharacteristicsInput | UnsetValueType = (
        DataclassValidator(VehicleCharacteristicsInput),
        Default(UnsetValue),
    )
    averageVehicleSpeed: SpeedValueInput | UnsetValueType = DataclassValidator(SpeedValueInput), Default(UnsetValue)
    speedPercentile: list[SpeedPercentileInput] | UnsetValueType = (
        ListValidator(DataclassValidator(SpeedPercentileInput)),
        Default(UnsetValue),
    )
    normallyExpectedSpeed: SpeedValueInput | UnsetValueType = DataclassValidator(SpeedValueInput), Default(UnsetValue)
    minimumSpeed: SpeedValueInput | UnsetValueType = DataclassValidator(SpeedValueInput), Default(UnsetValue)
    maximumSpeed: SpeedValueInput | UnsetValueType = DataclassValidator(SpeedValueInput), Default(UnsetValue)
    roaBasicDataExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    roaTrafficDataExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    roaTrafficSpeedExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
