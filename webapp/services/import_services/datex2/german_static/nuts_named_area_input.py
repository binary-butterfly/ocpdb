"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, StringValidator

from .extension_type_g_input import ExtensionTypeGInput
from .multilingual_string_input import MultilingualStringInput
from .named_area_type_enum_g_input import NamedAreaTypeEnumGInput
from .nuts_code_type_enum_g_input import NutsCodeTypeEnumGInput


@validataclass
class NutsNamedAreaInput:
    areaName: MultilingualStringInput = DataclassValidator(MultilingualStringInput)
    namedAreaType: NamedAreaTypeEnumGInput | UnsetValueType = (
        DataclassValidator(NamedAreaTypeEnumGInput),
        Default(UnsetValue),
    )
    country: str | UnsetValueType = StringValidator(max_length=2), Default(UnsetValue)
    nutsCodeType: NutsCodeTypeEnumGInput = DataclassValidator(NutsCodeTypeEnumGInput)
    nutsCode: str = StringValidator(max_length=5)
    comNamedAreaExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    locNamedAreaExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    locNutsNamedAreaExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
