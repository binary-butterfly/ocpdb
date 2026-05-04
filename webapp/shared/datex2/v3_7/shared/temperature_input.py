"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .extension_type_g_input import ExtensionTypeGInput
from .temperature_value_input import TemperatureValueInput


@validataclass
class TemperatureInput(ValidataclassMixin):
    airTemperature: TemperatureValueInput | UnsetValueType = (
        DataclassValidator(TemperatureValueInput),
        Default(UnsetValue),
    )
    dewPointTemperature: TemperatureValueInput | UnsetValueType = (
        DataclassValidator(TemperatureValueInput),
        Default(UnsetValue),
    )
    maximumTemperature: TemperatureValueInput | UnsetValueType = (
        DataclassValidator(TemperatureValueInput),
        Default(UnsetValue),
    )
    minimumTemperature: TemperatureValueInput | UnsetValueType = (
        DataclassValidator(TemperatureValueInput),
        Default(UnsetValue),
    )
    comTemperatureExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
