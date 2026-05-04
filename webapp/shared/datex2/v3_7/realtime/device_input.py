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
    IntegerValidator,
    ListValidator,
    StringValidator,
)

from webapp.shared.datex2.v3_7.shared.device_reference_g_input import DeviceReferenceGInput
from webapp.shared.datex2.v3_7.shared.device_type_enum_g_input import DeviceTypeEnumGInput
from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.international_identifier_input import InternationalIdentifierInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput
from webapp.shared.datex2.v3_7.shared.physical_device_details_input import PhysicalDeviceDetailsInput

from .component_input import ComponentInput
from .point_location_g_input import PointLocationGInput


@validataclass
class DeviceInput(ValidataclassMixin):
    idG: str = StringValidator()
    versionG: str = StringValidator()
    typeOfDevice: DeviceTypeEnumGInput = DataclassValidator(DeviceTypeEnumGInput)
    lastUpdateOfDeviceInformation: datetime = DateTimeValidator()
    externalDeviceId: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    lastDeviceCheck: datetime | UnsetValueType = DateTimeValidator(), Default(UnsetValue)
    softwareVersion: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    softwareVersionDate: datetime | UnsetValueType = DateTimeValidator(), Default(UnsetValue)
    additionalDeviceInformation: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    ipAddress: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    portNumber: int | UnsetValueType = IntegerValidator(min_value=0.0), Default(UnsetValue)
    accountableAuthority: InternationalIdentifierInput | UnsetValueType = (
        DataclassValidator(InternationalIdentifierInput),
        Default(UnsetValue),
    )
    pointLocation: PointLocationGInput = DataclassValidator(PointLocationGInput)
    physicalDeviceDetails: PhysicalDeviceDetailsInput | UnsetValueType = (
        DataclassValidator(PhysicalDeviceDetailsInput),
        Default(UnsetValue),
    )
    component: list[ComponentInput] | UnsetValueType = (
        ListValidator(DataclassValidator(ComponentInput)),
        Default(UnsetValue),
    )
    dependsOn: list[DeviceReferenceGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(DeviceReferenceGInput)),
        Default(UnsetValue),
    )
    fstDeviceExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
