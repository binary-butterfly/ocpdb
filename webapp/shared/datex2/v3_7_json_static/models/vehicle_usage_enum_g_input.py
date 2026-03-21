"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator

from .vehicle_usage_enum import VehicleUsageEnum
from .vehicle_usage_enum_extension_type_g import VehicleUsageEnumExtensionTypeG


@validataclass
class VehicleUsageEnumGInput(ValidataclassMixin):
    value: VehicleUsageEnum = EnumValidator(VehicleUsageEnum)
    extendedValueG: VehicleUsageEnumExtensionTypeG | UnsetValueType = (
        EnumValidator(VehicleUsageEnumExtensionTypeG),
        Default(UnsetValue),
    )
