"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, StringValidator

from .extension_type_g_input import ExtensionTypeGInput
from .gml_line_string_g_input import GmlLineStringGInput
from .linear_element_nature_enum_g_input import LinearElementNatureEnumGInput
from .multilingual_string_input import MultilingualStringInput


@validataclass
class LinearElementByLineStringInput(ValidataclassMixin):
    roadName: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    roadNumber: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    linearElementReferenceModel: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    linearElementReferenceModelVersion: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    linearElementNature: LinearElementNatureEnumGInput | UnsetValueType = (
        DataclassValidator(LinearElementNatureEnumGInput),
        Default(UnsetValue),
    )
    gmlLineString: GmlLineStringGInput = DataclassValidator(GmlLineStringGInput)
    locLinearElementExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    locLinearElementByLineStringExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
