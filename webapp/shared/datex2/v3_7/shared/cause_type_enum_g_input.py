"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator

from .cause_type_enum import CauseTypeEnum
from .cause_type_enum_extension_type_g import CauseTypeEnumExtensionTypeG


@validataclass
class CauseTypeEnumGInput(ValidataclassMixin):
    value: CauseTypeEnum = EnumValidator(CauseTypeEnum)
    extendedValueG: CauseTypeEnumExtensionTypeG | UnsetValueType = (
        EnumValidator(CauseTypeEnumExtensionTypeG),
        Default(UnsetValue),
    )
