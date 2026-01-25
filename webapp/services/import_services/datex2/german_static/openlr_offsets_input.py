"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, IntegerValidator

from .extension_type_g_input import ExtensionTypeGInput


@validataclass
class OpenlrOffsetsInput:
    openlrPositiveOffset: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    openlrNegativeOffset: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    locOpenlrOffsetsExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
