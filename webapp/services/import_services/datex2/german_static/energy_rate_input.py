"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import (
    BooleanValidator,
    DataclassValidator,
    FloatValidator,
    ListValidator,
    StringValidator,
)

from .energy_price_input import EnergyPriceInput
from .extension_type_g_input import ExtensionTypeGInput
from .multilingual_string_input import MultilingualStringInput
from .overall_period_input import OverallPeriodInput
from .payment_input import PaymentInput
from .rate_policy_enum_g_input import RatePolicyEnumGInput


@validataclass
class EnergyRateInput:
    idG: str = StringValidator()
    ratePolicy: RatePolicyEnumGInput = DataclassValidator(RatePolicyEnumGInput)
    lastUpdated: str = StringValidator()
    applicableCurrency: list[str] = ListValidator(StringValidator())
    rateName: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    combinationWithParkingFee: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    maximumDeliveryFee: int | UnsetValueType = FloatValidator(), Default(UnsetValue)
    minimumDeliveryFee: int | UnsetValueType = FloatValidator(), Default(UnsetValue)
    discount: int | UnsetValueType = FloatValidator(), Default(UnsetValue)
    additionalInformation: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    payment: PaymentInput | UnsetValueType = DataclassValidator(PaymentInput), Default(UnsetValue)
    energyPrice: list[EnergyPriceInput] | UnsetValueType = (
        ListValidator(DataclassValidator(EnergyPriceInput)),
        Default(UnsetValue),
    )
    overallPeriod: OverallPeriodInput | UnsetValueType = DataclassValidator(OverallPeriodInput), Default(UnsetValue)
    aegiEnergyRateExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
