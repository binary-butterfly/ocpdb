"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .extension_type_g_input import ExtensionTypeGInput
from .humidity_input import HumidityInput
from .measurement_or_calculation_time_input import MeasurementOrCalculationTimeInput


@validataclass
class HumidityInformationInput(ValidataclassMixin):
    measurementOrCalculationTime: MeasurementOrCalculationTimeInput | UnsetValueType = (
        DataclassValidator(MeasurementOrCalculationTimeInput),
        Default(UnsetValue),
    )
    humidity: HumidityInput = DataclassValidator(HumidityInput)
    roaBasicDataExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    roaWeatherDataExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    roaHumidityInformationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
