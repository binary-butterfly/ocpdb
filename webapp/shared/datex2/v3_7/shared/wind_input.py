"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, IntegerValidator

from .direction_bearing_value_input import DirectionBearingValueInput
from .direction_compass_value_input import DirectionCompassValueInput
from .extension_type_g_input import ExtensionTypeGInput
from .wind_speed_value_input import WindSpeedValueInput


@validataclass
class WindInput(ValidataclassMixin):
    windMeasurementHeight: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    windSpeed: WindSpeedValueInput | UnsetValueType = DataclassValidator(WindSpeedValueInput), Default(UnsetValue)
    maximumWindSpeed: WindSpeedValueInput | UnsetValueType = (
        DataclassValidator(WindSpeedValueInput),
        Default(UnsetValue),
    )
    windDirectionBearing: DirectionBearingValueInput | UnsetValueType = (
        DataclassValidator(DirectionBearingValueInput),
        Default(UnsetValue),
    )
    maximumWindDirectionBearing: DirectionBearingValueInput | UnsetValueType = (
        DataclassValidator(DirectionBearingValueInput),
        Default(UnsetValue),
    )
    windDirectionCompass: DirectionCompassValueInput | UnsetValueType = (
        DataclassValidator(DirectionCompassValueInput),
        Default(UnsetValue),
    )
    maximumWindDirectionCompass: DirectionCompassValueInput | UnsetValueType = (
        DataclassValidator(DirectionCompassValueInput),
        Default(UnsetValue),
    )
    comWindExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
