"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator, FloatValidator, ListValidator

from .extension_type_g_input import ExtensionTypeGInput
from .multilingual_string_input import MultilingualStringInput
from .pricing_policy_enum_g_input import PricingPolicyEnumGInput


@validataclass
class EnergyPricingPolicyInput(ValidataclassMixin):
    pricingPolicy: list[PricingPolicyEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(PricingPolicyEnumGInput)),
        Default(UnsetValue),
    )
    combinationWithParkingFee: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    discount: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    maximumDeliveryFee: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    minimumDeliveryFee: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    additionalInformation: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    egiEnergyPricingPolicyExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
