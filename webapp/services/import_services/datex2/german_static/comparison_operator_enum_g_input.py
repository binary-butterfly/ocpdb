"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator, StringValidator

from .comparison_operator_enum import ComparisonOperatorEnum


@validataclass
class ComparisonOperatorEnumGInput:
    value: ComparisonOperatorEnum = EnumValidator(ComparisonOperatorEnum)
    extendedValueG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
