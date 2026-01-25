"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator, StringValidator

from .openlr_functional_road_class_enum import OpenlrFunctionalRoadClassEnum


@validataclass
class OpenlrFunctionalRoadClassEnumGInput:
    value: OpenlrFunctionalRoadClassEnum = EnumValidator(OpenlrFunctionalRoadClassEnum)
    extendedValueG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
