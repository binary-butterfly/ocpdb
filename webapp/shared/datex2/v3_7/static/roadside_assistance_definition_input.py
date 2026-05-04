"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.roadside_assistance_type_enum_g_input import RoadsideAssistanceTypeEnumGInput

from .location_reference_g_input import LocationReferenceGInput


@validataclass
class RoadsideAssistanceDefinitionInput(ValidataclassMixin):
    roadsideAssistanceType: RoadsideAssistanceTypeEnumGInput = DataclassValidator(RoadsideAssistanceTypeEnumGInput)
    targetLocation: list[LocationReferenceGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(LocationReferenceGInput)),
        Default(UnsetValue),
    )
    tmpOperatorActionDefinitionExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    tmpRoadsideAssistanceDefinitionExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
