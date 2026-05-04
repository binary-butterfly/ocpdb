"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.measurement_or_calculation_time_input import MeasurementOrCalculationTimeInput
from webapp.shared.datex2.v3_7.shared.vehicle_flow_value_input import VehicleFlowValueInput

from .vehicle_characteristics_input import VehicleCharacteristicsInput


@validataclass
class VehicleRateInput(ValidataclassMixin):
    fillRate: VehicleFlowValueInput | UnsetValueType = DataclassValidator(VehicleFlowValueInput), Default(UnsetValue)
    exitRate: VehicleFlowValueInput | UnsetValueType = DataclassValidator(VehicleFlowValueInput), Default(UnsetValue)
    vehicleFlowRate: VehicleFlowValueInput | UnsetValueType = (
        DataclassValidator(VehicleFlowValueInput),
        Default(UnsetValue),
    )
    measuredVehicles: VehicleCharacteristicsInput | UnsetValueType = (
        DataclassValidator(VehicleCharacteristicsInput),
        Default(UnsetValue),
    )
    measurementOrCalculationTime: MeasurementOrCalculationTimeInput | UnsetValueType = (
        DataclassValidator(MeasurementOrCalculationTimeInput),
        Default(UnsetValue),
    )
    prkVehicleRateExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
