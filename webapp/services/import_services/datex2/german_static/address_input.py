"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator, StringValidator

from .address_line_input import AddressLineInput
from .extension_type_g_input import ExtensionTypeGInput
from .multilingual_string_input import MultilingualStringInput


@validataclass
class AddressInput:
    postcode: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    city: MultilingualStringInput | UnsetValueType = DataclassValidator(MultilingualStringInput), Default(UnsetValue)
    countryCode: str | UnsetValueType = StringValidator(max_length=2), Default(UnsetValue)
    addressLine: list[AddressLineInput] | UnsetValueType = (
        ListValidator(DataclassValidator(AddressLineInput)),
        Default(UnsetValue),
    )
    locxAddressExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
