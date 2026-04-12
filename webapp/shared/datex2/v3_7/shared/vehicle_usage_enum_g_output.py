"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .vehicle_usage_enum import VehicleUsageEnum
from .vehicle_usage_enum_extension_type_g import VehicleUsageEnumExtensionTypeG


@dataclass(kw_only=True)
class VehicleUsageEnumGOutput:
    value: VehicleUsageEnum
    extendedValueG: VehicleUsageEnumExtensionTypeG | None = None
