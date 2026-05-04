"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator, ListValidator, StringValidator

from webapp.shared.datex2.v3_7.shared.displayed_numerical_information_input import DisplayedNumericalInformationInput
from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.information_type_enum_g_input import InformationTypeEnumGInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput
from webapp.shared.datex2.v3_7.shared.pictogram_enum_g_input import PictogramEnumGInput

from .gdd_structure_input import GddStructureInput


@validataclass
class RegularPictogramInput(ValidataclassMixin):
    customPictogramCode: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    additionalDescription: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    pictogramFlashing: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    pictogramInInverseColour: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    viennaConventionCompliant: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    pictogramInformationType: InformationTypeEnumGInput | UnsetValueType = (
        DataclassValidator(InformationTypeEnumGInput),
        Default(UnsetValue),
    )
    pictogramDescription: list[PictogramEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(PictogramEnumGInput)),
        Default(UnsetValue),
    )
    presenceOfRedTriangle: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    gddStructure: GddStructureInput | UnsetValueType = DataclassValidator(GddStructureInput), Default(UnsetValue)
    displayedNumericalInformation: list[DisplayedNumericalInformationInput] | UnsetValueType = (
        ListValidator(DataclassValidator(DisplayedNumericalInformationInput)),
        Default(UnsetValue),
    )
    vmsPictogramExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    vmsRegularPictogramExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
