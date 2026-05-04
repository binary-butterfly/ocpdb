"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator, StringValidator

from .tpeg_loc04_height_type_enum import TpegLoc04HeightTypeEnum


@validataclass
class TpegLoc04HeightTypeEnumGInput(ValidataclassMixin):
    value: TpegLoc04HeightTypeEnum = EnumValidator(TpegLoc04HeightTypeEnum)
    extendedValueG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
