"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, IntegerValidator, StringValidator

from .extension_type_g_input import ExtensionTypeGInput


@validataclass
class GmlLineStringInput(ValidataclassMixin):
    """
    Line string based on GML (EN ISO 19136) definition: a curve defined by a series of two or more coordinate tuples. Unlike GML may be self-intersecting. If srsName attribute is not present, posList is assumed to use "ETRS89-LatLonh" reference system.
    """

    srsDimension: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    srsName: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    posList: str = StringValidator()
    locGmlLineStringExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
