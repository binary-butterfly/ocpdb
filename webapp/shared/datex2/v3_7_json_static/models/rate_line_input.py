"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import (
    DataclassValidator,
    FloatValidator,
    IntegerValidator,
    ListValidator,
    RegexValidator,
    StringValidator,
)

from .extension_type_g_input import ExtensionTypeGInput
from .multilingual_string_input import MultilingualStringInput
from .rate_line_tax_input import RateLineTaxInput
from .rate_line_type_enum_g_input import RateLineTypeEnumGInput
from .rate_usage_conditions_type_enum_g_input import RateUsageConditionsTypeEnumGInput
from .surcharge_input import SurchargeInput


@validataclass
class RateLineInput(ValidataclassMixin):
    """
    A specific rate element of a rate line collection within a specific rate table.
    """

    sequence: int = IntegerValidator()
    rateLineType: RateLineTypeEnumGInput = DataclassValidator(RateLineTypeEnumGInput)
    description: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    durationStart: str | UnsetValueType = (
        RegexValidator(
            pattern=r'^(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?|(24:00:00(\.0+)?))(Z|(\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00))?$'
        ),
        Default(UnsetValue),
    )
    durationEnd: str | UnsetValueType = (
        RegexValidator(
            pattern=r'^(([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9](\.[0-9]+)?|(24:00:00(\.0+)?))(Z|(\+|-)((0[0-9]|1[0-3]):[0-5][0-9]|14:00))?$'
        ),
        Default(UnsetValue),
    )
    incrementPeriod: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    value: int = FloatValidator()
    minValue: int | UnsetValueType = FloatValidator(), Default(UnsetValue)
    maxValue: int | UnsetValueType = FloatValidator(), Default(UnsetValue)
    usageCondition: RateUsageConditionsTypeEnumGInput | UnsetValueType = (
        DataclassValidator(RateUsageConditionsTypeEnumGInput),
        Default(UnsetValue),
    )
    surcharge: list[SurchargeInput] | UnsetValueType = (
        ListValidator(DataclassValidator(SurchargeInput)),
        Default(UnsetValue),
    )
    rateLineTax: list[RateLineTaxInput] | UnsetValueType = (
        ListValidator(DataclassValidator(RateLineTaxInput)),
        Default(UnsetValue),
    )
    facRateLineExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
