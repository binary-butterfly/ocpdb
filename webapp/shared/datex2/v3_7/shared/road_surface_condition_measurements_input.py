"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator

from .application_rate_value_input import ApplicationRateValueInput
from .extension_type_g_input import ExtensionTypeGInput
from .floating_point_metre_distance_value_input import FloatingPointMetreDistanceValueInput
from .friction_value_input import FrictionValueInput
from .kilograms_concentration_value_input import KilogramsConcentrationValueInput
from .percentage_value_input import PercentageValueInput
from .temperature_below_or_above_road_surface_input import TemperatureBelowOrAboveRoadSurfaceInput
from .temperature_value_input import TemperatureValueInput


@validataclass
class RoadSurfaceConditionMeasurementsInput(ValidataclassMixin):
    temperatureBelowOrAboveRoadSurface: list[TemperatureBelowOrAboveRoadSurfaceInput] | UnsetValueType = (
        ListValidator(DataclassValidator(TemperatureBelowOrAboveRoadSurfaceInput)),
        Default(UnsetValue),
    )
    roadSurfaceTemperature: TemperatureValueInput | UnsetValueType = (
        DataclassValidator(TemperatureValueInput),
        Default(UnsetValue),
    )
    protectionTemperature: TemperatureValueInput | UnsetValueType = (
        DataclassValidator(TemperatureValueInput),
        Default(UnsetValue),
    )
    deIcingApplicationRate: ApplicationRateValueInput | UnsetValueType = (
        DataclassValidator(ApplicationRateValueInput),
        Default(UnsetValue),
    )
    deIcingConcentration: KilogramsConcentrationValueInput | UnsetValueType = (
        DataclassValidator(KilogramsConcentrationValueInput),
        Default(UnsetValue),
    )
    friction: FrictionValueInput | UnsetValueType = DataclassValidator(FrictionValueInput), Default(UnsetValue)
    depthOfSnow: FloatingPointMetreDistanceValueInput | UnsetValueType = (
        DataclassValidator(FloatingPointMetreDistanceValueInput),
        Default(UnsetValue),
    )
    waterFilmThickness: FloatingPointMetreDistanceValueInput | UnsetValueType = (
        DataclassValidator(FloatingPointMetreDistanceValueInput),
        Default(UnsetValue),
    )
    iceLayerThickness: FloatingPointMetreDistanceValueInput | UnsetValueType = (
        DataclassValidator(FloatingPointMetreDistanceValueInput),
        Default(UnsetValue),
    )
    icePercentage: PercentageValueInput | UnsetValueType = DataclassValidator(PercentageValueInput), Default(UnsetValue)
    comRoadSurfaceConditionMeasurementsExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
