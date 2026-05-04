"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator

from .vehicle_equipment_enum import VehicleEquipmentEnum
from .vehicle_equipment_enum_extension_type_g import VehicleEquipmentEnumExtensionTypeG


@validataclass
class VehicleEquipmentEnumGInput(ValidataclassMixin):
    value: VehicleEquipmentEnum = EnumValidator(VehicleEquipmentEnum)
    extendedValueG: VehicleEquipmentEnumExtensionTypeG | UnsetValueType = (
        EnumValidator(VehicleEquipmentEnumExtensionTypeG),
        Default(UnsetValue),
    )
