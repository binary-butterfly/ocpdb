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
class EnergyRateInput(ValidataclassMixin):
    idG: str = StringValidator()
    ratePolicy: RatePolicyEnumGInput = DataclassValidator(RatePolicyEnumGInput)
    lastUpdated: datetime = DateTimeValidator()
    applicableCurrency: list[str] = ListValidator(StringValidator())
    rateName: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    combinationWithParkingFee: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    maximumDeliveryFee: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    minimumDeliveryFee: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    discount: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
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
