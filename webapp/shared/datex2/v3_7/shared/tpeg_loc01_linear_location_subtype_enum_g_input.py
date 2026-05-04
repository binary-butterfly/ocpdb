"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator, StringValidator

from .tpeg_loc01_linear_location_subtype_enum import TpegLoc01LinearLocationSubtypeEnum


@validataclass
class TpegLoc01LinearLocationSubtypeEnumGInput(ValidataclassMixin):
    value: TpegLoc01LinearLocationSubtypeEnum = EnumValidator(TpegLoc01LinearLocationSubtypeEnum)
    extendedValueG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
