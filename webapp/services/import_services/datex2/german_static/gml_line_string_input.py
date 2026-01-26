"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, IntegerValidator, StringValidator

from .extension_type_g_input import ExtensionTypeGInput


@validataclass
class GmlLineStringInput:
    srsDimension: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    srsName: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    posList: str = StringValidator()
    locGmlLineStringExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
