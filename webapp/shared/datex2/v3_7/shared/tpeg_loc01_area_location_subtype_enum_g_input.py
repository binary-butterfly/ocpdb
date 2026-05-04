"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator, StringValidator

from .tpeg_loc01_area_location_subtype_enum import TpegLoc01AreaLocationSubtypeEnum


@validataclass
class TpegLoc01AreaLocationSubtypeEnumGInput(ValidataclassMixin):
    value: TpegLoc01AreaLocationSubtypeEnum = EnumValidator(TpegLoc01AreaLocationSubtypeEnum)
    extendedValueG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
