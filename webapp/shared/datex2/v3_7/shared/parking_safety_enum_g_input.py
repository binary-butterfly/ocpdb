"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator, StringValidator

from .parking_safety_enum import ParkingSafetyEnum


@validataclass(reject_unknown_fields=True)
class ParkingSafetyEnumGInput(ValidataclassMixin):
    value: ParkingSafetyEnum = EnumValidator(ParkingSafetyEnum)
    extendedValueG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
