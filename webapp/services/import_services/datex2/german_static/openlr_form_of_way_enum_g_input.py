"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator, StringValidator

from .openlr_form_of_way_enum import OpenlrFormOfWayEnum


@validataclass
class OpenlrFormOfWayEnumGInput:
    value: OpenlrFormOfWayEnum = EnumValidator(OpenlrFormOfWayEnum)
    extendedValueG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
