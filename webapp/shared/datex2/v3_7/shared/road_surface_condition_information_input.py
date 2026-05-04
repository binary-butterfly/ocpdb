"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator

from .extension_type_g_input import ExtensionTypeGInput
from .measurement_or_calculation_time_input import MeasurementOrCalculationTimeInput
from .road_surface_condition_measurements_input import RoadSurfaceConditionMeasurementsInput
from .weather_related_road_condition_type_enum_g_input import WeatherRelatedRoadConditionTypeEnumGInput


@validataclass
class RoadSurfaceConditionInformationInput(ValidataclassMixin):
    weatherRelatedRoadConditionType: list[WeatherRelatedRoadConditionTypeEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(WeatherRelatedRoadConditionTypeEnumGInput)),
        Default(UnsetValue),
    )
    measurementOrCalculationTime: MeasurementOrCalculationTimeInput | UnsetValueType = (
        DataclassValidator(MeasurementOrCalculationTimeInput),
        Default(UnsetValue),
    )
    roadSurfaceConditionMeasurements: RoadSurfaceConditionMeasurementsInput = DataclassValidator(
        RoadSurfaceConditionMeasurementsInput
    )
    roaBasicDataExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    roaWeatherDataExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    roaRoadSurfaceConditionInformationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
