"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator

from .general_instruction_to_road_users_type_enum import GeneralInstructionToRoadUsersTypeEnum
from .general_instruction_to_road_users_type_enum_extension_type_g import (
    GeneralInstructionToRoadUsersTypeEnumExtensionTypeG,
)


@validataclass
class GeneralInstructionToRoadUsersTypeEnumGInput(ValidataclassMixin):
    value: GeneralInstructionToRoadUsersTypeEnum = EnumValidator(GeneralInstructionToRoadUsersTypeEnum)
    extendedValueG: GeneralInstructionToRoadUsersTypeEnumExtensionTypeG | UnsetValueType = (
        EnumValidator(GeneralInstructionToRoadUsersTypeEnumExtensionTypeG),
        Default(UnsetValue),
    )
