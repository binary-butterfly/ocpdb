"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator, StringValidator

from .traffic_status_enum import TrafficStatusEnum


@validataclass
class TrafficStatusEnumGInput(ValidataclassMixin):
    value: TrafficStatusEnum = EnumValidator(TrafficStatusEnum)
    extendedValueG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
