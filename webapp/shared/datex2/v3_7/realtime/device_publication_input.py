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

from .device_g_input import DeviceGInput
from .device_table_input import DeviceTableInput


@validataclass
class DevicePublicationInput(ValidataclassMixin):
    lang: str = RegexValidator(pattern=r'^[a-z]{2}$')
    feedDescription: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    feedType: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    publicationTime: datetime = DateTimeValidator()
    publicationCreator: InternationalIdentifierInput = DataclassValidator(InternationalIdentifierInput)
    headerInformation: HeaderInformationInput = DataclassValidator(HeaderInformationInput)
    device: list[DeviceGInput] | UnsetValueType = ListValidator(DataclassValidator(DeviceGInput)), Default(UnsetValue)
    deviceTable: list[DeviceTableInput] | UnsetValueType = (
        ListValidator(DataclassValidator(DeviceTableInput)),
        Default(UnsetValue),
    )
    comPayloadPublicationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    fstDevicePublicationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
