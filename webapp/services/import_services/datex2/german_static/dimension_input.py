"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, FloatValidator, IntegerValidator

from .extension_type_g_input import ExtensionTypeGInput


@validataclass
class DimensionInput:
    length: int | UnsetValueType = FloatValidator(), Default(UnsetValue)
    width: int | UnsetValueType = FloatValidator(), Default(UnsetValue)
    height: int | UnsetValueType = FloatValidator(), Default(UnsetValue)
    usableArea: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    afacDimensionExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
