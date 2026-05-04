"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator

from .device_table_reference_g_input import DeviceTableReferenceGInput
from .extension_type_g_input import ExtensionTypeGInput
from .status_input import StatusInput


@validataclass
class StatusOfAllDevicesFromTableInput(ValidataclassMixin):
    deviceTableReference: DeviceTableReferenceGInput = DataclassValidator(DeviceTableReferenceGInput)
    status: list[StatusInput] = ListValidator(DataclassValidator(StatusInput))
    fstStatusOfAllDevicesFromTableExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
