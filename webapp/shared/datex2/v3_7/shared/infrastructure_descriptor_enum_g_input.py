"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator

from .infrastructure_descriptor_enum import InfrastructureDescriptorEnum
from .infrastructure_descriptor_enum_extension_type_g import InfrastructureDescriptorEnumExtensionTypeG


@validataclass
class InfrastructureDescriptorEnumGInput(ValidataclassMixin):
    value: InfrastructureDescriptorEnum = EnumValidator(InfrastructureDescriptorEnum)
    extendedValueG: InfrastructureDescriptorEnumExtensionTypeG | UnsetValueType = (
        EnumValidator(InfrastructureDescriptorEnumExtensionTypeG),
        Default(UnsetValue),
    )
