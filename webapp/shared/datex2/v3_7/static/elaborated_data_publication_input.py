"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from datetime import datetime

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import (
    BooleanValidator,
    DataclassValidator,
    DateTimeValidator,
    FloatValidator,
    ListValidator,
    RegexValidator,
    StringValidator,
)

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.header_information_input import HeaderInformationInput
from webapp.shared.datex2.v3_7.shared.international_identifier_input import InternationalIdentifierInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput
from webapp.shared.datex2.v3_7.shared.reference_settings_input import ReferenceSettingsInput

from .physical_quantity_g_input import PhysicalQuantityGInput


@validataclass
class ElaboratedDataPublicationInput(ValidataclassMixin):
    lang: str = RegexValidator(pattern=r'^[a-z]{2}$')
    feedDescription: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    feedType: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    publicationTime: datetime = DateTimeValidator()
    forecastDefault: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    periodDefault: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    timeDefault: datetime | UnsetValueType = DateTimeValidator(), Default(UnsetValue)
    publicationCreator: InternationalIdentifierInput = DataclassValidator(InternationalIdentifierInput)
    headerInformation: HeaderInformationInput = DataclassValidator(HeaderInformationInput)
    referenceSettings: ReferenceSettingsInput | UnsetValueType = (
        DataclassValidator(ReferenceSettingsInput),
        Default(UnsetValue),
    )
    physicalQuantity: list[PhysicalQuantityGInput] = ListValidator(DataclassValidator(PhysicalQuantityGInput))
    informationManager: InternationalIdentifierInput | UnsetValueType = (
        DataclassValidator(InternationalIdentifierInput),
        Default(UnsetValue),
    )
    comPayloadPublicationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    roaElaboratedDataPublicationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
