"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator

from .vehicle_type_enum import VehicleTypeEnum
from .vehicle_type_enum_extension_type_g import VehicleTypeEnumExtensionTypeG


@validataclass
class VehicleTypeEnumGInput(ValidataclassMixin):
    value: VehicleTypeEnum = EnumValidator(VehicleTypeEnum)
    extendedValueG: VehicleTypeEnumExtensionTypeG | UnsetValueType = (
        EnumValidator(VehicleTypeEnumExtensionTypeG),
        Default(UnsetValue),
    )
