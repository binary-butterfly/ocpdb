"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator, StringValidator

from .tpeg_loc03_ilc_point_descriptor_subtype_enum import TpegLoc03IlcPointDescriptorSubtypeEnum


@validataclass
class TpegLoc03IlcPointDescriptorSubtypeEnumGInput(ValidataclassMixin):
    value: TpegLoc03IlcPointDescriptorSubtypeEnum = EnumValidator(TpegLoc03IlcPointDescriptorSubtypeEnum)
    extendedValueG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
