"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator

from .equipment_or_system_type_enum import EquipmentOrSystemTypeEnum
from .equipment_or_system_type_enum_extension_type_g import EquipmentOrSystemTypeEnumExtensionTypeG


@validataclass
class EquipmentOrSystemTypeEnumGInput(ValidataclassMixin):
    value: EquipmentOrSystemTypeEnum = EnumValidator(EquipmentOrSystemTypeEnum)
    extendedValueG: EquipmentOrSystemTypeEnumExtensionTypeG | UnsetValueType = (
        EnumValidator(EquipmentOrSystemTypeEnumExtensionTypeG),
        Default(UnsetValue),
    )
