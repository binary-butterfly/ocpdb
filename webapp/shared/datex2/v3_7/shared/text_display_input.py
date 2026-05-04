"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator, ListValidator, StringValidator

from .extension_type_g_input import ExtensionTypeGInput
from .multilingual_string_input import MultilingualStringInput
from .text_display_line_index_text_line_g_input import textDisplayLineIndexTextLineGInput


@validataclass
class TextDisplayInput(ValidataclassMixin):
    isBlank: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    legallyBinding: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    legalBasis: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    textCode: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    textImageUrl: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    textLine: list[textDisplayLineIndexTextLineGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(textDisplayLineIndexTextLineGInput)),
        Default(UnsetValue),
    )
    vmsDisplayAreaSettingsExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    vmsTextDisplayExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
