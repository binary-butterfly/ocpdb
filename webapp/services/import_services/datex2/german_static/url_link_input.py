"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, StringValidator

from .extension_type_g_input import ExtensionTypeGInput
from .multilingual_string_input import MultilingualStringInput
from .url_link_type_enum_g_input import UrlLinkTypeEnumGInput


@validataclass
class UrlLinkInput:
    urlLinkAddress: str = StringValidator()
    urlLinkDescription: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    urlLinkType: UrlLinkTypeEnumGInput | UnsetValueType = DataclassValidator(UrlLinkTypeEnumGInput), Default(UnsetValue)
    comUrlLinkExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
