"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator

from .infrastructure_damage_type_enum import InfrastructureDamageTypeEnum
from .infrastructure_damage_type_enum_extension_type_g import InfrastructureDamageTypeEnumExtensionTypeG


@validataclass
class InfrastructureDamageTypeEnumGInput(ValidataclassMixin):
    value: InfrastructureDamageTypeEnum = EnumValidator(InfrastructureDamageTypeEnum)
    extendedValueG: InfrastructureDamageTypeEnumExtensionTypeG | UnsetValueType = (
        EnumValidator(InfrastructureDamageTypeEnumExtensionTypeG),
        Default(UnsetValue),
    )
