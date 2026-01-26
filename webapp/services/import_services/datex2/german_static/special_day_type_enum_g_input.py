"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator, StringValidator

from .special_day_type_enum import SpecialDayTypeEnum


@validataclass
class SpecialDayTypeEnumGInput:
    value: SpecialDayTypeEnum = EnumValidator(SpecialDayTypeEnum)
    extendedValueG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
