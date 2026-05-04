"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator

from .brands_accepted_code_list_input import BrandsAcceptedCodeListInput
from .brands_accepted_text_input import BrandsAcceptedTextInput
from .extension_type_g_input import ExtensionTypeGInput
from .means_of_payment_enum_g_input import MeansOfPaymentEnumGInput
from .payment_timing_enum_g_input import PaymentTimingEnumGInput


@validataclass
class PaymentMethodInput(ValidataclassMixin):
    paymentMeans: list[MeansOfPaymentEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(MeansOfPaymentEnumGInput)),
        Default(UnsetValue),
    )
    paymentMode: list[PaymentTimingEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(PaymentTimingEnumGInput)),
        Default(UnsetValue),
    )
    brandsAcceptedText: list[BrandsAcceptedTextInput] | UnsetValueType = (
        ListValidator(DataclassValidator(BrandsAcceptedTextInput)),
        Default(UnsetValue),
    )
    brandsAcceptedCodeList: list[BrandsAcceptedCodeListInput] | UnsetValueType = (
        ListValidator(DataclassValidator(BrandsAcceptedCodeListInput)),
        Default(UnsetValue),
    )
    facPaymentMethodExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
