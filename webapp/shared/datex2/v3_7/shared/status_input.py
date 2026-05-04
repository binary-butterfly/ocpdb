"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from datetime import datetime

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, DateTimeValidator, ListValidator

from .catalogue_information_input import CatalogueInformationInput
from .device_health_enum_g_input import DeviceHealthEnumGInput
from .device_power_input import DevicePowerInput
from .device_reference_g_input import DeviceReferenceGInput
from .extension_type_g_input import ExtensionTypeGInput
from .multilingual_string_input import MultilingualStringInput
from .operational_state_input import OperationalStateInput
from .versioned_reference_input import VersionedReferenceInput


@validataclass
class StatusInput(ValidataclassMixin):
    health: DeviceHealthEnumGInput = DataclassValidator(DeviceHealthEnumGInput)
    statusDescription: list[MultilingualStringInput] | UnsetValueType = (
        ListValidator(DataclassValidator(MultilingualStringInput)),
        Default(UnsetValue),
    )
    lastStatusChange: datetime | UnsetValueType = DateTimeValidator(), Default(UnsetValue)
    lastStatusUpdate: datetime = DateTimeValidator()
    relatedFault: list[VersionedReferenceInput] | UnsetValueType = (
        ListValidator(DataclassValidator(VersionedReferenceInput)),
        Default(UnsetValue),
    )
    deviceReference: DeviceReferenceGInput = DataclassValidator(DeviceReferenceGInput)
    operationalState: OperationalStateInput | UnsetValueType = (
        DataclassValidator(OperationalStateInput),
        Default(UnsetValue),
    )
    statusCatalogueInformation: CatalogueInformationInput | UnsetValueType = (
        DataclassValidator(CatalogueInformationInput),
        Default(UnsetValue),
    )
    devicePower: list[DevicePowerInput] | UnsetValueType = (
        ListValidator(DataclassValidator(DevicePowerInput)),
        Default(UnsetValue),
    )
    fstStatusExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
