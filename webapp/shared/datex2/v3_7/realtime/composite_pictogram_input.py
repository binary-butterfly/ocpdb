"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator, StringValidator

from webapp.shared.datex2.v3_7.shared.composite_pictogram_enum_g_input import CompositePictogramEnumGInput
from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.information_type_enum_g_input import InformationTypeEnumGInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput

from .gdd_structure_input import GddStructureInput
from .regular_pictogram_input import RegularPictogramInput


@validataclass
class CompositePictogramInput(ValidataclassMixin):
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
    pictogramDescription: CompositePictogramEnumGInput = DataclassValidator(CompositePictogramEnumGInput)
    gddStructure: GddStructureInput | UnsetValueType = DataclassValidator(GddStructureInput), Default(UnsetValue)
    regularPictogram: RegularPictogramInput = DataclassValidator(RegularPictogramInput)
    vmsPictogramExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    vmsCompositePictogramExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
