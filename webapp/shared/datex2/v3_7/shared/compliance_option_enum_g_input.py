"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator

from .compliance_option_enum import ComplianceOptionEnum
from .compliance_option_enum_extension_type_g import ComplianceOptionEnumExtensionTypeG


@validataclass
class ComplianceOptionEnumGInput(ValidataclassMixin):
    value: ComplianceOptionEnum = EnumValidator(ComplianceOptionEnum)
    extendedValueG: ComplianceOptionEnumExtensionTypeG | UnsetValueType = (
        EnumValidator(ComplianceOptionEnumExtensionTypeG),
        Default(UnsetValue),
    )
