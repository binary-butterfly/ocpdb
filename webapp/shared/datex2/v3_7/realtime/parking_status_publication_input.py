"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from datetime import datetime

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import (
    DataclassValidator,
    DateTimeValidator,
    ListValidator,
    RegexValidator,
    StringValidator,
)

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.header_information_input import HeaderInformationInput
from webapp.shared.datex2.v3_7.shared.international_identifier_input import InternationalIdentifierInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput
from webapp.shared.datex2.v3_7.shared.parking_table_versioned_reference_g_input import (
    ParkingTableVersionedReferenceGInput,
)

from .parking_status_information_g_input import ParkingStatusInformationGInput


@validataclass
class ParkingStatusPublicationInput(ValidataclassMixin):
    lang: str = RegexValidator(pattern=r'^[a-z]{2}$')
    feedDescription: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    feedType: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    publicationTime: datetime = DateTimeValidator()
    parkingTableReference: list[ParkingTableVersionedReferenceGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(ParkingTableVersionedReferenceGInput)),
        Default(UnsetValue),
    )
    publicationCreator: InternationalIdentifierInput = DataclassValidator(InternationalIdentifierInput)
    headerInformation: HeaderInformationInput | UnsetValueType = (
        DataclassValidator(HeaderInformationInput),
        Default(UnsetValue),
    )
    parkingStatusInformation: list[ParkingStatusInformationGInput] = ListValidator(
        DataclassValidator(ParkingStatusInformationGInput)
    )
    comPayloadPublicationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    prkParkingStatusPublicationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
