"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator, StringValidator

from .environmental_obstruction_type_enum import EnvironmentalObstructionTypeEnum


@validataclass
class EnvironmentalObstructionTypeEnumGInput(ValidataclassMixin):
    value: EnvironmentalObstructionTypeEnum = EnumValidator(EnvironmentalObstructionTypeEnum)
    extendedValueG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
