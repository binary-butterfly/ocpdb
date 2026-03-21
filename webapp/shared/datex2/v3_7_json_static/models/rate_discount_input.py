"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, FloatValidator

from .amount_in_currency_input import AmountInCurrencyInput
from .extension_type_g_input import ExtensionTypeGInput


@validataclass
class RateDiscountInput(ValidataclassMixin):
    """
    Class defining discount rates to be applied to a RateTable
    """

    discountRate: int | UnsetValueType = FloatValidator(), Default(UnsetValue)
    fixedValue: AmountInCurrencyInput | UnsetValueType = DataclassValidator(AmountInCurrencyInput), Default(UnsetValue)
    facRateDiscountExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
