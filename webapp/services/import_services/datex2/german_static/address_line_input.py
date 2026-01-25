"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, IntegerValidator

from .address_line_type_enum_g_input import AddressLineTypeEnumGInput
from .extension_type_g_input import ExtensionTypeGInput
from .multilingual_string_input import MultilingualStringInput


@validataclass
class AddressLineInput:
    order: int = IntegerValidator(min_value=0)
    type: AddressLineTypeEnumGInput = DataclassValidator(AddressLineTypeEnumGInput)
    text: MultilingualStringInput = DataclassValidator(MultilingualStringInput)
    locxAddressLineExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
