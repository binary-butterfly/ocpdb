"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, StringValidator

from .extension_type_g_input import ExtensionTypeGInput
from .multilingual_string_input import MultilingualStringInput
from .named_area_extension_type_g_input import NamedAreaExtensionTypeGInput
from .named_area_type_enum_g_input import NamedAreaTypeEnumGInput


@validataclass
class NamedAreaInput(ValidataclassMixin):
    """
    An area defined by a name and/or in terms of known boundaries, such as country or county boundaries or allocated control area of particular authority. The attributes do not form a union; instead, the smallest intersection forms the resulting area.
    """

    areaName: MultilingualStringInput = DataclassValidator(MultilingualStringInput)
    namedAreaType: NamedAreaTypeEnumGInput | UnsetValueType = (
        DataclassValidator(NamedAreaTypeEnumGInput),
        Default(UnsetValue),
    )
    country: str | UnsetValueType = StringValidator(max_length=2), Default(UnsetValue)
    comNamedAreaExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    locNamedAreaExtensionG: NamedAreaExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(NamedAreaExtensionTypeGInput),
        Default(UnsetValue),
    )
