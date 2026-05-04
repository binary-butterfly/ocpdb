"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .extension_type_g_input import ExtensionTypeGInput
from .user_type_enum_g_input import UserTypeEnumGInput


@validataclass
class UserQualificationInput(ValidataclassMixin):
    userGroup: UserTypeEnumGInput = DataclassValidator(UserTypeEnumGInput)
    afacUserQualificationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
