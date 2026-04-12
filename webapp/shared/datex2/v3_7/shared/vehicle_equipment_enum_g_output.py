"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .vehicle_equipment_enum import VehicleEquipmentEnum
from .vehicle_equipment_enum_extension_type_g import VehicleEquipmentEnumExtensionTypeG


@dataclass(kw_only=True)
class VehicleEquipmentEnumGOutput:
    value: VehicleEquipmentEnum
    extendedValueG: VehicleEquipmentEnumExtensionTypeG | None = None
