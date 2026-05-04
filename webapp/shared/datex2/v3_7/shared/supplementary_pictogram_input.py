"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator, StringValidator

from .extension_type_g_input import ExtensionTypeGInput
from .information_type_enum_g_input import InformationTypeEnumGInput
from .multilingual_string_input import MultilingualStringInput
from .supplemental_pictogram_enum_g_input import SupplementalPictogramEnumGInput


@validataclass
class SupplementaryPictogramInput(ValidataclassMixin):
    isBlank: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    legallyBinding: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    legalBasis: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    pictogramDescription: SupplementalPictogramEnumGInput | UnsetValueType = (
        DataclassValidator(SupplementalPictogramEnumGInput),
        Default(UnsetValue),
    )
    pictogramCode: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    pictogramUrl: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    additionalDescription: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    pictogramFlashing: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    pictogramInformationType: InformationTypeEnumGInput | UnsetValueType = (
        DataclassValidator(InformationTypeEnumGInput),
        Default(UnsetValue),
    )
    vmsDisplayAreaSettingsExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    vmsSupplementaryInformationDisplayExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    vmsSupplementaryPictogramExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
