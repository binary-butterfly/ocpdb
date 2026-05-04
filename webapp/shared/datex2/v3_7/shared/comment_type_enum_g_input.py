"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator

from .comment_type_enum import CommentTypeEnum
from .comment_type_enum_extension_type_g import CommentTypeEnumExtensionTypeG


@validataclass
class CommentTypeEnumGInput(ValidataclassMixin):
    value: CommentTypeEnum = EnumValidator(CommentTypeEnum)
    extendedValueG: CommentTypeEnumExtensionTypeG | UnsetValueType = (
        EnumValidator(CommentTypeEnumExtensionTypeG),
        Default(UnsetValue),
    )
