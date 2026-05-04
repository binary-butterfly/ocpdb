"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator

from .load_type_enum import LoadTypeEnum
from .load_type_enum_extension_type_g import LoadTypeEnumExtensionTypeG


@validataclass
class LoadTypeEnumGInput(ValidataclassMixin):
    value: LoadTypeEnum = EnumValidator(LoadTypeEnum)
    extendedValueG: LoadTypeEnumExtensionTypeG | UnsetValueType = (
        EnumValidator(LoadTypeEnumExtensionTypeG),
        Default(UnsetValue),
    )
