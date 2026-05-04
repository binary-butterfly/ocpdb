"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator

from .general_network_management_type_enum import GeneralNetworkManagementTypeEnum
from .general_network_management_type_enum_extension_type_g import GeneralNetworkManagementTypeEnumExtensionTypeG


@validataclass
class GeneralNetworkManagementTypeEnumGInput(ValidataclassMixin):
    value: GeneralNetworkManagementTypeEnum = EnumValidator(GeneralNetworkManagementTypeEnum)
    extendedValueG: GeneralNetworkManagementTypeEnumExtensionTypeG | UnsetValueType = (
        EnumValidator(GeneralNetworkManagementTypeEnumExtensionTypeG),
        Default(UnsetValue),
    )
