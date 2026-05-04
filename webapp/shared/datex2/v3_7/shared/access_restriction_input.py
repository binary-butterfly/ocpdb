"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .access_restriction_type_enum_g_input import AccessRestrictionTypeEnumGInput
from .extension_type_g_input import ExtensionTypeGInput


@validataclass
class AccessRestrictionInput(ValidataclassMixin):
    accessRestrictionType: AccessRestrictionTypeEnumGInput = DataclassValidator(AccessRestrictionTypeEnumGInput)
    troTypeOfRegulationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    troAccessRestrictionExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
