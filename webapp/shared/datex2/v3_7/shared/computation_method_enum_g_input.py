"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator, StringValidator

from .computation_method_enum import ComputationMethodEnum


@validataclass
class ComputationMethodEnumGInput(ValidataclassMixin):
    value: ComputationMethodEnum = EnumValidator(ComputationMethodEnum)
    extendedValueG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
