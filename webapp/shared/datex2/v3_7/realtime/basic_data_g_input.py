"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from webapp.shared.datex2.v3_7.shared.humidity_information_input import HumidityInformationInput
from webapp.shared.datex2.v3_7.shared.pollution_information_input import PollutionInformationInput
from webapp.shared.datex2.v3_7.shared.precipitation_information_input import PrecipitationInformationInput
from webapp.shared.datex2.v3_7.shared.pressure_information_input import PressureInformationInput
from webapp.shared.datex2.v3_7.shared.road_surface_condition_information_input import (
    RoadSurfaceConditionInformationInput,
)
from webapp.shared.datex2.v3_7.shared.temperature_information_input import TemperatureInformationInput
from webapp.shared.datex2.v3_7.shared.traffic_status_input import TrafficStatusInput
from webapp.shared.datex2.v3_7.shared.travel_time_data_input import TravelTimeDataInput
from webapp.shared.datex2.v3_7.shared.visibility_information_input import VisibilityInformationInput
from webapp.shared.datex2.v3_7.shared.wind_information_input import WindInformationInput

from .individual_vehicle_data_values_input import IndividualVehicleDataValuesInput
from .traffic_concentration_input import TrafficConcentrationInput
from .traffic_flow_input import TrafficFlowInput
from .traffic_gap_input import TrafficGapInput
from .traffic_headway_input import TrafficHeadwayInput
from .traffic_speed_input import TrafficSpeedInput


@validataclass
class BasicDataGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    roaTrafficStatus: TrafficStatusInput | UnsetValueType = DataclassValidator(TrafficStatusInput), Default(UnsetValue)
    roaTravelTimeData: TravelTimeDataInput | UnsetValueType = (
        DataclassValidator(TravelTimeDataInput),
        Default(UnsetValue),
    )
    roaPrecipitationInformation: PrecipitationInformationInput | UnsetValueType = (
        DataclassValidator(PrecipitationInformationInput),
        Default(UnsetValue),
    )
    roaHumidityInformation: HumidityInformationInput | UnsetValueType = (
        DataclassValidator(HumidityInformationInput),
        Default(UnsetValue),
    )
    roaWindInformation: WindInformationInput | UnsetValueType = (
        DataclassValidator(WindInformationInput),
        Default(UnsetValue),
    )
    roaVisibilityInformation: VisibilityInformationInput | UnsetValueType = (
        DataclassValidator(VisibilityInformationInput),
        Default(UnsetValue),
    )
    roaPollutionInformation: PollutionInformationInput | UnsetValueType = (
        DataclassValidator(PollutionInformationInput),
        Default(UnsetValue),
    )
    roaRoadSurfaceConditionInformation: RoadSurfaceConditionInformationInput | UnsetValueType = (
        DataclassValidator(RoadSurfaceConditionInformationInput),
        Default(UnsetValue),
    )
    roaTemperatureInformation: TemperatureInformationInput | UnsetValueType = (
        DataclassValidator(TemperatureInformationInput),
        Default(UnsetValue),
    )
    roaPressureInformation: PressureInformationInput | UnsetValueType = (
        DataclassValidator(PressureInformationInput),
        Default(UnsetValue),
    )
    roaTrafficGap: TrafficGapInput | UnsetValueType = DataclassValidator(TrafficGapInput), Default(UnsetValue)
    roaTrafficFlow: TrafficFlowInput | UnsetValueType = DataclassValidator(TrafficFlowInput), Default(UnsetValue)
    roaTrafficSpeed: TrafficSpeedInput | UnsetValueType = DataclassValidator(TrafficSpeedInput), Default(UnsetValue)
    roaTrafficHeadway: TrafficHeadwayInput | UnsetValueType = (
        DataclassValidator(TrafficHeadwayInput),
        Default(UnsetValue),
    )
    roaTrafficConcentration: TrafficConcentrationInput | UnsetValueType = (
        DataclassValidator(TrafficConcentrationInput),
        Default(UnsetValue),
    )
    roaIndividualVehicleDataValues: IndividualVehicleDataValuesInput | UnsetValueType = (
        DataclassValidator(IndividualVehicleDataValuesInput),
        Default(UnsetValue),
    )
