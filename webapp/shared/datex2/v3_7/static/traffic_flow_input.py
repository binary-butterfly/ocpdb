"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from webapp.shared.datex2.v3_7.shared.axle_characteristics_input import AxleCharacteristicsInput
from webapp.shared.datex2.v3_7.shared.axle_flow_value_input import AxleFlowValueInput
from webapp.shared.datex2.v3_7.shared.daily_traffic_flow_value_input import DailyTrafficFlowValueInput
from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.measurement_or_calculation_time_input import MeasurementOrCalculationTimeInput
from webapp.shared.datex2.v3_7.shared.pcu_flow_value_input import PcuFlowValueInput
from webapp.shared.datex2.v3_7.shared.percentage_value_input import PercentageValueInput
from webapp.shared.datex2.v3_7.shared.vehicle_flow_value_input import VehicleFlowValueInput

from .vehicle_characteristics_input import VehicleCharacteristicsInput


@validataclass
class TrafficFlowInput(ValidataclassMixin):
    measurementOrCalculationTime: MeasurementOrCalculationTimeInput | UnsetValueType = (
        DataclassValidator(MeasurementOrCalculationTimeInput),
        Default(UnsetValue),
    )
    forVehiclesWithCharacteristicsOf: VehicleCharacteristicsInput | UnsetValueType = (
        DataclassValidator(VehicleCharacteristicsInput),
        Default(UnsetValue),
    )
    axleFlow: AxleFlowValueInput | UnsetValueType = DataclassValidator(AxleFlowValueInput), Default(UnsetValue)
    pcuFlow: PcuFlowValueInput | UnsetValueType = DataclassValidator(PcuFlowValueInput), Default(UnsetValue)
    percentageLongVehicles: PercentageValueInput | UnsetValueType = (
        DataclassValidator(PercentageValueInput),
        Default(UnsetValue),
    )
    vehicleFlow: VehicleFlowValueInput | UnsetValueType = DataclassValidator(VehicleFlowValueInput), Default(UnsetValue)
    normallyExpectedFlow: VehicleFlowValueInput | UnsetValueType = (
        DataclassValidator(VehicleFlowValueInput),
        Default(UnsetValue),
    )
    annualAverageDailyTraffic: DailyTrafficFlowValueInput | UnsetValueType = (
        DataclassValidator(DailyTrafficFlowValueInput),
        Default(UnsetValue),
    )
    monthlyAverageDailyTraffic: DailyTrafficFlowValueInput | UnsetValueType = (
        DataclassValidator(DailyTrafficFlowValueInput),
        Default(UnsetValue),
    )
    axleCharacteristics: AxleCharacteristicsInput | UnsetValueType = (
        DataclassValidator(AxleCharacteristicsInput),
        Default(UnsetValue),
    )
    roaBasicDataExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    roaTrafficDataExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    roaTrafficFlowExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
