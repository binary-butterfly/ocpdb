"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .device_health_enum_g_input import DeviceHealthEnumGInput
from .extension_type_g_input import ExtensionTypeGInput
from .power_source_enum_g_input import PowerSourceEnumGInput


@validataclass
class DevicePowerInput(ValidataclassMixin):
    health: DeviceHealthEnumGInput = DataclassValidator(DeviceHealthEnumGInput)
    sourceType: PowerSourceEnumGInput = DataclassValidator(PowerSourceEnumGInput)
    fstDevicePowerExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
