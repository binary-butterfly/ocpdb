"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator, StringValidator

from .applicable_days_within_month_enum import ApplicableDaysWithinMonthEnum


@validataclass
class ApplicableDaysWithinMonthEnumGInput(ValidataclassMixin):
    value: ApplicableDaysWithinMonthEnum = EnumValidator(ApplicableDaysWithinMonthEnum)
    extendedValueG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
