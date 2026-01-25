"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator, StringValidator

from .confidentiality_value_enum import ConfidentialityValueEnum


@validataclass
class ConfidentialityValueEnumGInput:
    value: ConfidentialityValueEnum = EnumValidator(ConfidentialityValueEnum)
    extendedValueG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
