"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .application_rate_value_input import ApplicationRateValueInput
from .direction_bearing_value_input import DirectionBearingValueInput
from .direction_compass_value_input import DirectionCompassValueInput
from .floating_point_metre_distance_value_input import FloatingPointMetreDistanceValueInput
from .friction_value_input import FrictionValueInput
from .integer_metre_distance_value_input import IntegerMetreDistanceValueInput
from .kilograms_concentration_value_input import KilogramsConcentrationValueInput
from .micrograms_concentration_value_input import MicrogramsConcentrationValueInput
from .percentage_value_input import PercentageValueInput
from .precipitation_intensity_value_input import PrecipitationIntensityValueInput
from .pressure_value_input import PressureValueInput
from .temperature_value_input import TemperatureValueInput
from .vehicle_flow_value_input import VehicleFlowValueInput
from .wind_speed_value_input import WindSpeedValueInput


@validataclass
class DataValueGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    comKilogramsConcentrationValue: KilogramsConcentrationValueInput | UnsetValueType = (
        DataclassValidator(KilogramsConcentrationValueInput),
        Default(UnsetValue),
    )
    comApplicationRateValue: ApplicationRateValueInput | UnsetValueType = (
        DataclassValidator(ApplicationRateValueInput),
        Default(UnsetValue),
    )
    comPercentageValue: PercentageValueInput | UnsetValueType = (
        DataclassValidator(PercentageValueInput),
        Default(UnsetValue),
    )
    comFrictionValue: FrictionValueInput | UnsetValueType = DataclassValidator(FrictionValueInput), Default(UnsetValue)
    comMicrogramsConcentrationValue: MicrogramsConcentrationValueInput | UnsetValueType = (
        DataclassValidator(MicrogramsConcentrationValueInput),
        Default(UnsetValue),
    )
    comWindSpeedValue: WindSpeedValueInput | UnsetValueType = (
        DataclassValidator(WindSpeedValueInput),
        Default(UnsetValue),
    )
    comTemperatureValue: TemperatureValueInput | UnsetValueType = (
        DataclassValidator(TemperatureValueInput),
        Default(UnsetValue),
    )
    comVehicleFlowValue: VehicleFlowValueInput | UnsetValueType = (
        DataclassValidator(VehicleFlowValueInput),
        Default(UnsetValue),
    )
    comDirectionCompassValue: DirectionCompassValueInput | UnsetValueType = (
        DataclassValidator(DirectionCompassValueInput),
        Default(UnsetValue),
    )
    comDirectionBearingValue: DirectionBearingValueInput | UnsetValueType = (
        DataclassValidator(DirectionBearingValueInput),
        Default(UnsetValue),
    )
    comIntegerMetreDistanceValue: IntegerMetreDistanceValueInput | UnsetValueType = (
        DataclassValidator(IntegerMetreDistanceValueInput),
        Default(UnsetValue),
    )
    comPressureValue: PressureValueInput | UnsetValueType = DataclassValidator(PressureValueInput), Default(UnsetValue)
    comFloatingPointMetreDistanceValue: FloatingPointMetreDistanceValueInput | UnsetValueType = (
        DataclassValidator(FloatingPointMetreDistanceValueInput),
        Default(UnsetValue),
    )
    comPrecipitationIntensityValue: PrecipitationIntensityValueInput | UnsetValueType = (
        DataclassValidator(PrecipitationIntensityValueInput),
        Default(UnsetValue),
    )
