"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator, StringValidator

from .operational_device_state_enum import OperationalDeviceStateEnum


@validataclass
class OperationalDeviceStateEnumGInput(ValidataclassMixin):
    value: OperationalDeviceStateEnum = EnumValidator(OperationalDeviceStateEnum)
    extendedValueG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
