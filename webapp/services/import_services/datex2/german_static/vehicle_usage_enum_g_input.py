"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator, StringValidator

from .vehicle_usage_enum import VehicleUsageEnum


@validataclass
class VehicleUsageEnumGInput:
    value: VehicleUsageEnum = EnumValidator(VehicleUsageEnum)
    extendedValueG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
