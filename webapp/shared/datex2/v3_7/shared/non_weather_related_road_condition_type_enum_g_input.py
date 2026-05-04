"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator, StringValidator

from .non_weather_related_road_condition_type_enum import NonWeatherRelatedRoadConditionTypeEnum


@validataclass
class NonWeatherRelatedRoadConditionTypeEnumGInput(ValidataclassMixin):
    value: NonWeatherRelatedRoadConditionTypeEnum = EnumValidator(NonWeatherRelatedRoadConditionTypeEnum)
    extendedValueG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
