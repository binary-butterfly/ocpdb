"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator, RegexValidator, StringValidator

from .extension_type_g_input import ExtensionTypeGInput


@validataclass
class ContactInformationInput:
    language: list[str] | UnsetValueType = ListValidator(RegexValidator(pattern=r'^[a-z]{2}$')), Default(UnsetValue)
    telephoneNumber: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    faxNumber: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    eMail: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    afacContactInformationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
