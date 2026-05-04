"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from datetime import datetime

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import (
    BooleanValidator,
    DataclassValidator,
    DateTimeValidator,
    FloatValidator,
    IntegerValidator,
    ListValidator,
    RegexValidator,
    StringValidator,
)

from .extension_type_g_input import ExtensionTypeGInput
from .rate_line_input import RateLineInput


@validataclass
class RelativeTimeRatesInput(ValidataclassMixin):
    collectionSequence: int = IntegerValidator()
    applicableCurrency: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    minValueCollection: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    maxValueCollection: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    validStart: datetime | UnsetValueType = DateTimeValidator(), Default(UnsetValue)
    validEnd: datetime | UnsetValueType = DateTimeValidator(), Default(UnsetValue)
    minTime: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    maxTime: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    resetTime: str | UnsetValueType = (
        RegexValidator(
            pattern=r'^(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?|(24:00:00(\.0+)?))(Z|(\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00))?$'
        ),
        Default(UnsetValue),
    )
    taxIncluded: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    taxRate: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    taxValue: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    relativeTimes: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    referenceTimeStart: datetime | UnsetValueType = DateTimeValidator(), Default(UnsetValue)
    referenceTimeEnd: datetime | UnsetValueType = DateTimeValidator(), Default(UnsetValue)
    rateLine: list[RateLineInput] = ListValidator(DataclassValidator(RateLineInput))
    afacRateLineCollectionExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    afacRelativeTimeRatesExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
