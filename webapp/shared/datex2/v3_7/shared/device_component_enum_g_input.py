"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator, StringValidator

from .device_component_enum import DeviceComponentEnum


@validataclass
class DeviceComponentEnumGInput(ValidataclassMixin):
    value: DeviceComponentEnum = EnumValidator(DeviceComponentEnum)
    extendedValueG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
