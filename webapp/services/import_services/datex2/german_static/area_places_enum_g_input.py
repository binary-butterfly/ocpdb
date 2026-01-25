"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator, StringValidator

from .area_places_enum import AreaPlacesEnum


@validataclass
class AreaPlacesEnumGInput:
    value: AreaPlacesEnum = EnumValidator(AreaPlacesEnum)
    extendedValueG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
