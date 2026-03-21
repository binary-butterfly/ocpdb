"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator, StringValidator

from .direction_compass_enum import DirectionCompassEnum


@validataclass
class DirectionCompassEnumGInput(ValidataclassMixin):
    value: DirectionCompassEnum = EnumValidator(DirectionCompassEnum)
    extendedValueG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
