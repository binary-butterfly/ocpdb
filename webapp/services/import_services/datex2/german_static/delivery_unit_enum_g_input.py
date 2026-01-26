"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator, StringValidator

from .delivery_unit_enum import DeliveryUnitEnum


@validataclass
class DeliveryUnitEnumGInput:
    value: DeliveryUnitEnum = EnumValidator(DeliveryUnitEnum)
    extendedValueG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
