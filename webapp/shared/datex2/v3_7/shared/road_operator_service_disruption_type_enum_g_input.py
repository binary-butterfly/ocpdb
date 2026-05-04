"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator, StringValidator

from .road_operator_service_disruption_type_enum import RoadOperatorServiceDisruptionTypeEnum


@validataclass
class RoadOperatorServiceDisruptionTypeEnumGInput(ValidataclassMixin):
    value: RoadOperatorServiceDisruptionTypeEnum = EnumValidator(RoadOperatorServiceDisruptionTypeEnum)
    extendedValueG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
