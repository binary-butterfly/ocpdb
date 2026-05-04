"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from datetime import datetime

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, DateTimeValidator

from .extension_type_g_input import ExtensionTypeGInput
from .period_input import PeriodInput
from .time_meaning_enum_g_input import TimeMeaningEnumGInput
from .time_precision_enum_g_input import TimePrecisionEnumGInput


@validataclass
class MeasurementOrCalculationTimeInput(ValidataclassMixin):
    timeMeaning: TimeMeaningEnumGInput | UnsetValueType = DataclassValidator(TimeMeaningEnumGInput), Default(UnsetValue)
    timePrecision: TimePrecisionEnumGInput | UnsetValueType = (
        DataclassValidator(TimePrecisionEnumGInput),
        Default(UnsetValue),
    )
    timeValue: datetime | UnsetValueType = DateTimeValidator(), Default(UnsetValue)
    period: PeriodInput | UnsetValueType = DataclassValidator(PeriodInput), Default(UnsetValue)
    roaMeasurementOrCalculationTimeExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
