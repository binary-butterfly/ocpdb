"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator, IntegerValidator, ListValidator

from .extension_type_g_input import ExtensionTypeGInput
from .multi_page_display_page_number_display_area_settings_g_input import (
    multiPageDisplayPageNumberDisplayAreaSettingsGInput,
)
from .multilingual_string_input import MultilingualStringInput


@validataclass
class MultiPageDisplayInput(ValidataclassMixin):
    isBlank: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    legallyBinding: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    legalBasis: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    sequenceGroupNumber: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    displayAreaSettings: list[multiPageDisplayPageNumberDisplayAreaSettingsGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(multiPageDisplayPageNumberDisplayAreaSettingsGInput)),
        Default(UnsetValue),
    )
    vmsDisplayAreaSettingsExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    vmsMultiPageDisplayExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
