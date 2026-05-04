"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, FloatValidator, ListValidator

from .extension_type_g_input import ExtensionTypeGInput
from .hydrogen_refuelling_mode_enum_g_input import HydrogenRefuellingModeEnumGInput


@validataclass
class HydrogenInput(ValidataclassMixin):
    refuellingMode: list[HydrogenRefuellingModeEnumGInput] = ListValidator(
        DataclassValidator(HydrogenRefuellingModeEnumGInput)
    )
    cumulativeCapacityperDay: float = FloatValidator(allow_integers=True)
    aegiHydrogenExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
