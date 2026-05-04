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

from .all_faults_of_single_device_input import AllFaultsOfSingleDeviceInput
from .extension_type_g_input import ExtensionTypeGInput
from .faults_of_all_devices_from_table_input import FaultsOfAllDevicesFromTableInput
from .header_information_input import HeaderInformationInput
from .international_identifier_input import InternationalIdentifierInput
from .multilingual_string_input import MultilingualStringInput


@validataclass
class FaultPublicationInput(ValidataclassMixin):
    lang: str = RegexValidator(pattern=r'^[a-z]{2}$')
    feedDescription: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    feedType: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    publicationTime: datetime = DateTimeValidator()
    publicationCreator: InternationalIdentifierInput = DataclassValidator(InternationalIdentifierInput)
    headerInformation: HeaderInformationInput = DataclassValidator(HeaderInformationInput)
    allFaultsOfSingleDevice: list[AllFaultsOfSingleDeviceInput] | UnsetValueType = (
        ListValidator(DataclassValidator(AllFaultsOfSingleDeviceInput)),
        Default(UnsetValue),
    )
    faultsOfAllDevicesFromTable: list[FaultsOfAllDevicesFromTableInput] | UnsetValueType = (
        ListValidator(DataclassValidator(FaultsOfAllDevicesFromTableInput)),
        Default(UnsetValue),
    )
    comPayloadPublicationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    fstFaultPublicationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
