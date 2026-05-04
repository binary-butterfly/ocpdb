"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator, StringValidator

from .extension_type_g_input import ExtensionTypeGInput
from .multilingual_string_input import MultilingualStringInput
from .source_type_enum_g_input import SourceTypeEnumGInput


@validataclass
class SourceInput(ValidataclassMixin):
    sourceCountry: str | UnsetValueType = StringValidator(max_length=2), Default(UnsetValue)
    sourceIdentification: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    sourceName: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    sourceType: SourceTypeEnumGInput | UnsetValueType = DataclassValidator(SourceTypeEnumGInput), Default(UnsetValue)
    reliable: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    comSourceExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
