"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator, StringValidator

from .standing_or_parking_control_type_enum import StandingOrParkingControlTypeEnum


@validataclass
class StandingOrParkingControlTypeEnumGInput(ValidataclassMixin):
    value: StandingOrParkingControlTypeEnum = EnumValidator(StandingOrParkingControlTypeEnum)
    extendedValueG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
