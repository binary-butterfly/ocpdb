"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import (
    BooleanValidator,
    DataclassValidator,
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
    """
    A class supporting the specification of times for defining rate applicability that are relative to a defined referenceTimeStart of an event.
    """

    collectionSequence: int = IntegerValidator()
    applicableCurrency: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    minValueCollection: float | UnsetValueType = FloatValidator(), Default(UnsetValue)
    maxValueCollection: float | UnsetValueType = FloatValidator(), Default(UnsetValue)
    validStart: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    validEnd: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    minTime: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    maxTime: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    resetTime: str | UnsetValueType = (
        RegexValidator(
            pattern=r'^(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?|(24:00:00(\.0+)?))(Z|(\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00))?$'
        ),
        Default(UnsetValue),
    )
    taxIncluded: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    taxRate: float | UnsetValueType = FloatValidator(), Default(UnsetValue)
    taxValue: float | UnsetValueType = FloatValidator(), Default(UnsetValue)
    relativeTimes: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    referenceTimeStart: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    referenceTimeEnd: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    rateLine: list[RateLineInput] = ListValidator(DataclassValidator(RateLineInput))
    facRateLineCollectionExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    facRelativeTimeRatesExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
