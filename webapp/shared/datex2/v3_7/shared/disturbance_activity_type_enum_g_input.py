"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator, StringValidator

from .disturbance_activity_type_enum import DisturbanceActivityTypeEnum


@validataclass
class DisturbanceActivityTypeEnumGInput(ValidataclassMixin):
    value: DisturbanceActivityTypeEnum = EnumValidator(DisturbanceActivityTypeEnum)
    extendedValueG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
