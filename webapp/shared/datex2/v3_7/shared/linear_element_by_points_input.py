"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator, StringValidator

from .extension_type_g_input import ExtensionTypeGInput
from .intermediate_point_on_linear_element_g_input import intermediatePointOnLinearElementGInput
from .linear_element_nature_enum_g_input import LinearElementNatureEnumGInput
from .multilingual_string_input import MultilingualStringInput
from .referent_input import ReferentInput


@validataclass
class LinearElementByPointsInput(ValidataclassMixin):
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
    startPointOfLinearElement: ReferentInput = DataclassValidator(ReferentInput)
    intermediatePointOnLinearElement: list[intermediatePointOnLinearElementGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(intermediatePointOnLinearElementGInput)),
        Default(UnsetValue),
    )
    endPointOfLinearElement: ReferentInput = DataclassValidator(ReferentInput)
    locLinearElementExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    locLinearElementByPointsExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
