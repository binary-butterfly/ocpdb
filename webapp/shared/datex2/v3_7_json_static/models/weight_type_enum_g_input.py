"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator

from .weight_type_enum import WeightTypeEnum
from .weight_type_enum_extension_type_g import WeightTypeEnumExtensionTypeG


@validataclass
class WeightTypeEnumGInput(ValidataclassMixin):
    value: WeightTypeEnum = EnumValidator(WeightTypeEnum)
    extendedValueG: WeightTypeEnumExtensionTypeG | UnsetValueType = (
        EnumValidator(WeightTypeEnumExtensionTypeG),
        Default(UnsetValue),
    )
