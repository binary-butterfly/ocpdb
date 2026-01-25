"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator

from .type_of_identifier_enum import TypeOfIdentifierEnum
from .type_of_identifier_enum_extension_type_g import TypeOfIdentifierEnumExtensionTypeG


@validataclass
class TypeOfIdentifierEnumGInput:
    value: TypeOfIdentifierEnum = EnumValidator(TypeOfIdentifierEnum)
    extendedValueG: TypeOfIdentifierEnumExtensionTypeG | UnsetValueType = (
        EnumValidator(TypeOfIdentifierEnumExtensionTypeG),
        Default(UnsetValue),
    )
