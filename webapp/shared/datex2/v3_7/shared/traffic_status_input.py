"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .extension_type_g_input import ExtensionTypeGInput
from .measurement_or_calculation_time_input import MeasurementOrCalculationTimeInput
from .traffic_status_value_input import TrafficStatusValueInput
from .traffic_trend_type_enum_g_input import TrafficTrendTypeEnumGInput


@validataclass
class TrafficStatusInput(ValidataclassMixin):
    trafficTrendType: TrafficTrendTypeEnumGInput | UnsetValueType = (
        DataclassValidator(TrafficTrendTypeEnumGInput),
        Default(UnsetValue),
    )
    measurementOrCalculationTime: MeasurementOrCalculationTimeInput | UnsetValueType = (
        DataclassValidator(MeasurementOrCalculationTimeInput),
        Default(UnsetValue),
    )
    trafficStatus: TrafficStatusValueInput | UnsetValueType = (
        DataclassValidator(TrafficStatusValueInput),
        Default(UnsetValue),
    )
    roaBasicDataExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    roaTrafficStatusExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
