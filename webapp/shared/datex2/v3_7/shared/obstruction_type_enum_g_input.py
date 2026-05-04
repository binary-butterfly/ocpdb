"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator

from .obstruction_type_enum import ObstructionTypeEnum
from .obstruction_type_enum_extension_type_g import ObstructionTypeEnumExtensionTypeG


@validataclass
class ObstructionTypeEnumGInput(ValidataclassMixin):
    value: ObstructionTypeEnum = EnumValidator(ObstructionTypeEnum)
    extendedValueG: ObstructionTypeEnumExtensionTypeG | UnsetValueType = (
        EnumValidator(ObstructionTypeEnumExtensionTypeG),
        Default(UnsetValue),
    )
