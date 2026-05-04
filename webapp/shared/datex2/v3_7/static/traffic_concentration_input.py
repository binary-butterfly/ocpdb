"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.measurement_or_calculation_time_input import MeasurementOrCalculationTimeInput
from webapp.shared.datex2.v3_7.shared.percentage_value_input import PercentageValueInput
from webapp.shared.datex2.v3_7.shared.traffic_density_value_input import TrafficDensityValueInput

from .vehicle_characteristics_input import VehicleCharacteristicsInput


@validataclass
class TrafficConcentrationInput(ValidataclassMixin):
    measurementOrCalculationTime: MeasurementOrCalculationTimeInput | UnsetValueType = (
        DataclassValidator(MeasurementOrCalculationTimeInput),
        Default(UnsetValue),
    )
    forVehiclesWithCharacteristicsOf: VehicleCharacteristicsInput | UnsetValueType = (
        DataclassValidator(VehicleCharacteristicsInput),
        Default(UnsetValue),
    )
    density: TrafficDensityValueInput | UnsetValueType = (
        DataclassValidator(TrafficDensityValueInput),
        Default(UnsetValue),
    )
    occupancy: PercentageValueInput | UnsetValueType = DataclassValidator(PercentageValueInput), Default(UnsetValue)
    roaBasicDataExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    roaTrafficDataExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    roaTrafficConcentrationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
