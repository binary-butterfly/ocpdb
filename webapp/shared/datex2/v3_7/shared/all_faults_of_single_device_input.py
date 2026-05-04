"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from datetime import datetime

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, DateTimeValidator, ListValidator

from .device_fault_input import DeviceFaultInput
from .device_reference_g_input import DeviceReferenceGInput
from .extension_type_g_input import ExtensionTypeGInput


@validataclass
class AllFaultsOfSingleDeviceInput(ValidataclassMixin):
    operatingProperlySince: datetime | UnsetValueType = DateTimeValidator(), Default(UnsetValue)
    deviceReference: DeviceReferenceGInput = DataclassValidator(DeviceReferenceGInput)
    deviceFault: list[DeviceFaultInput] | UnsetValueType = (
        ListValidator(DataclassValidator(DeviceFaultInput)),
        Default(UnsetValue),
    )
    fstAllFaultsOfSingleDeviceExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
