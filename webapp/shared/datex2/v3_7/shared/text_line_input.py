"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import (
    BooleanValidator,
    DataclassValidator,
    ListValidator,
    RegexValidator,
    StringValidator,
)

from .colour_enum_g_input import ColourEnumGInput
from .extension_type_g_input import ExtensionTypeGInput
from .information_type_enum_g_input import InformationTypeEnumGInput


@validataclass
class TextLineInput(ValidataclassMixin):
    textLine: str = StringValidator()
    lineLanguage: str | UnsetValueType = RegexValidator(pattern=r'^[a-z]{2}$'), Default(UnsetValue)
    lineColour: ColourEnumGInput | UnsetValueType = DataclassValidator(ColourEnumGInput), Default(UnsetValue)
    lineFlashing: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    lineHtml: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    isExactTextOnSign: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    textInformationType: list[InformationTypeEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(InformationTypeEnumGInput)),
        Default(UnsetValue),
    )
    vmsTextLineExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
