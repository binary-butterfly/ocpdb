"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator, StringValidator

from .extension_type_g_input import ExtensionTypeGInput
from .junction_classification_enum_g_input import JunctionClassificationEnumGInput
from .multilingual_string_input import MultilingualStringInput
from .road_information_g_input import RoadInformationGInput


@validataclass
class JunctionInformationInput(ValidataclassMixin):
    junctionClassification: JunctionClassificationEnumGInput | UnsetValueType = (
        DataclassValidator(JunctionClassificationEnumGInput),
        Default(UnsetValue),
    )
    junctionName: MultilingualStringInput = DataclassValidator(MultilingualStringInput)
    junctionNumber: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    motorway: RoadInformationGInput | UnsetValueType = DataclassValidator(RoadInformationGInput), Default(UnsetValue)
    intersectionDestinationMotorway: list[RoadInformationGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(RoadInformationGInput)),
        Default(UnsetValue),
    )
    prkJunctionInformationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
