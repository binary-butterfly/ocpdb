"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator, StringValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.image_input import ImageInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput
from webapp.shared.datex2.v3_7.shared.supplementary_information_display_g_input import (
    SupplementaryInformationDisplayGInput,
)

from .pictogram_g_input import PictogramGInput


@validataclass
class PictogramDisplayInput(ValidataclassMixin):
    isBlank: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    legallyBinding: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    legalBasis: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    isPrimaryPictogram: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    pictogramDisplayUrl: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    pictogram: PictogramGInput = DataclassValidator(PictogramGInput)
    supplementaryInformationDisplay: SupplementaryInformationDisplayGInput | UnsetValueType = (
        DataclassValidator(SupplementaryInformationDisplayGInput),
        Default(UnsetValue),
    )
    image: ImageInput | UnsetValueType = DataclassValidator(ImageInput), Default(UnsetValue)
    vmsDisplayAreaSettingsExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    vmsPictogramDisplayExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
