"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator, StringValidator

from .measured_or_derived_data_type_enum import MeasuredOrDerivedDataTypeEnum


@validataclass
class MeasuredOrDerivedDataTypeEnumGInput(ValidataclassMixin):
    value: MeasuredOrDerivedDataTypeEnum = EnumValidator(MeasuredOrDerivedDataTypeEnum)
    extendedValueG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
