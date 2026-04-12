"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .vehicle_type_enum import VehicleTypeEnum
from .vehicle_type_enum_extension_type_g import VehicleTypeEnumExtensionTypeG


@dataclass(kw_only=True)
class VehicleTypeEnumGOutput:
    value: VehicleTypeEnum
    extendedValueG: VehicleTypeEnumExtensionTypeG | None = None
