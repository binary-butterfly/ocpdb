"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator, StringValidator

from .extension_type_g_input import ExtensionTypeGInput
from .means_of_payment_enum_g_input import MeansOfPaymentEnumGInput
from .multilingual_string_input import MultilingualStringInput
from .payment_brands_enum_g_input import PaymentBrandsEnumGInput
from .payment_mode_enum_g_input import PaymentModeEnumGInput


@validataclass
class PaymentInput:
    paymentMode: list[PaymentModeEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(PaymentModeEnumGInput)),
        Default(UnsetValue),
    )
    paymentMeans: list[MeansOfPaymentEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(MeansOfPaymentEnumGInput)),
        Default(UnsetValue),
    )
    otherPaymentMeans: list[MultilingualStringInput] | UnsetValueType = (
        ListValidator(DataclassValidator(MultilingualStringInput)),
        Default(UnsetValue),
    )
    brandsAccepted: list[PaymentBrandsEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(PaymentBrandsEnumGInput)),
        Default(UnsetValue),
    )
    otherBrandsAccepted: list[str] | UnsetValueType = ListValidator(StringValidator()), Default(UnsetValue)
    afacPaymentExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
