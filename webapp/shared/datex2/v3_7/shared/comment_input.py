"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from datetime import datetime

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, DateTimeValidator

from .comment_type_enum_g_input import CommentTypeEnumGInput
from .extension_type_g_input import ExtensionTypeGInput
from .multilingual_string_input import MultilingualStringInput


@validataclass
class CommentInput(ValidataclassMixin):
    comment: MultilingualStringInput = DataclassValidator(MultilingualStringInput)
    commentDateTime: datetime | UnsetValueType = DateTimeValidator(), Default(UnsetValue)
    commentType: CommentTypeEnumGInput | UnsetValueType = DataclassValidator(CommentTypeEnumGInput), Default(UnsetValue)
    sitCommentExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
