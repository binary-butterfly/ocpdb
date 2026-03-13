"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator, RegexValidator, StringValidator

from .extension_type_g_input import ExtensionTypeGInput
from .multilingual_string_input import MultilingualStringInput


@validataclass
class ContactPersonInput:
    language: list[str] | UnsetValueType = ListValidator(RegexValidator(pattern=r'^[a-z]{2}$')), Default(UnsetValue)
    telephoneNumber: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    faxNumber: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    eMail: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    name: str = StringValidator()
    firstName: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    title: MultilingualStringInput | UnsetValueType = DataclassValidator(MultilingualStringInput), Default(UnsetValue)
    position: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    afacContactInformationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    afacContactPersonExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
