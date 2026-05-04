"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator

from .extension_type_g_input import ExtensionTypeGInput
from .measurement_or_calculation_time_input import MeasurementOrCalculationTimeInput
from .pollution_input import PollutionInput


@validataclass
class PollutionInformationInput(ValidataclassMixin):
    measurementOrCalculationTime: MeasurementOrCalculationTimeInput | UnsetValueType = (
        DataclassValidator(MeasurementOrCalculationTimeInput),
        Default(UnsetValue),
    )
    pollution: list[PollutionInput] = ListValidator(DataclassValidator(PollutionInput))
    roaBasicDataExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    roaWeatherDataExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    roaPollutionInformationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
