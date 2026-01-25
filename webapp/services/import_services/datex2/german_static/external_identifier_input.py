"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, StringValidator

from .extension_type_g_input import ExtensionTypeGInput
from .type_of_identifier_enum_g_input import TypeOfIdentifierEnumGInput


@validataclass
class ExternalIdentifierInput:
    identifier: str = StringValidator()
    typeOfIdentifier: TypeOfIdentifierEnumGInput | UnsetValueType = (
        DataclassValidator(TypeOfIdentifierEnumGInput),
        Default(UnsetValue),
    )
    otherTypeOfIdentifier: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    afacExternalIdentifierExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
