"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator

from .extension_type_g_input import ExtensionTypeGInput
from .multilingual_string_input import MultilingualStringInput
from .text_line_input import TextLineInput


@validataclass
class SupplementaryTextInput(ValidataclassMixin):
    isBlank: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    legallyBinding: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    legalBasis: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    textLine: TextLineInput = DataclassValidator(TextLineInput)
    vmsDisplayAreaSettingsExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    vmsSupplementaryInformationDisplayExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    vmsSupplementaryTextExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
