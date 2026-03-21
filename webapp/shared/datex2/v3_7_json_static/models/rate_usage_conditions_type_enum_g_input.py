"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator, StringValidator

from .rate_usage_conditions_type_enum import RateUsageConditionsTypeEnum


@validataclass
class RateUsageConditionsTypeEnumGInput(ValidataclassMixin):
    value: RateUsageConditionsTypeEnum = EnumValidator(RateUsageConditionsTypeEnum)
    extendedValueG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
