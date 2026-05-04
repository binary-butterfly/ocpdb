"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator, StringValidator

from .extension_type_g_input import ExtensionTypeGInput
from .multilingual_string_input import MultilingualStringInput
from .road_type_enum_g_input import RoadTypeEnumGInput


@validataclass
class RoadInformationEnhancedInput(ValidataclassMixin):
    roadDestination: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    roadName: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    roadNumber: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    typeOfRoad: RoadTypeEnumGInput | UnsetValueType = DataclassValidator(RoadTypeEnumGInput), Default(UnsetValue)
    roadOrigination: list[MultilingualStringInput] | UnsetValueType = (
        ListValidator(DataclassValidator(MultilingualStringInput)),
        Default(UnsetValue),
    )
    locRoadInformationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    prkRoadInformationEnhancedExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
