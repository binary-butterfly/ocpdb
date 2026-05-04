"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator, RegexValidator, StringValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput

from .gdd_pictogram_identification_input import GddPictogramIdentificationInput
from .point_location_g_input import PointLocationGInput


@validataclass
class SupplementaryPanelInput(ValidataclassMixin):
    pictureOfRoadSign: str | UnsetValueType = RegexValidator(pattern=r'^[A-Za-z0-9+/]+={0,2}$'), Default(UnsetValue)
    urlToRoadSign: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    nationalSignID: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    description: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    gddPictogramIdentification: GddPictogramIdentificationInput | UnsetValueType = (
        DataclassValidator(GddPictogramIdentificationInput),
        Default(UnsetValue),
    )
    locationOfSign: list[PointLocationGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(PointLocationGInput)),
        Default(UnsetValue),
    )
    troRoadSignExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    troSupplementaryPanelExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
