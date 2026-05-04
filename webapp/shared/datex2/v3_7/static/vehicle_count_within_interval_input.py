"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, FloatValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.measurement_or_calculation_time_input import MeasurementOrCalculationTimeInput
from webapp.shared.datex2.v3_7.shared.occupancy_change_value_input import OccupancyChangeValueInput
from webapp.shared.datex2.v3_7.shared.vehicle_count_value_input import VehicleCountValueInput

from .vehicle_characteristics_input import VehicleCharacteristicsInput


@validataclass
class VehicleCountWithinIntervalInput(ValidataclassMixin):
    measurementInterval: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    numberOfIncomingVehicles: VehicleCountValueInput | UnsetValueType = (
        DataclassValidator(VehicleCountValueInput),
        Default(UnsetValue),
    )
    numberOfOutgoingVehicles: VehicleCountValueInput | UnsetValueType = (
        DataclassValidator(VehicleCountValueInput),
        Default(UnsetValue),
    )
    changeOfOccupiedSpaces: OccupancyChangeValueInput | UnsetValueType = (
        DataclassValidator(OccupancyChangeValueInput),
        Default(UnsetValue),
    )
    countedVehicles: VehicleCharacteristicsInput | UnsetValueType = (
        DataclassValidator(VehicleCharacteristicsInput),
        Default(UnsetValue),
    )
    measurementOrCalculationTime: MeasurementOrCalculationTimeInput | UnsetValueType = (
        DataclassValidator(MeasurementOrCalculationTimeInput),
        Default(UnsetValue),
    )
    prkVehicleCountWithinIntervalExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
