"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .fuel_type_enum import FuelTypeEnum
from .fuel_type_enum_extension_type_g import FuelTypeEnumExtensionTypeG


@dataclass(kw_only=True)
class FuelTypeEnumGOutput:
    value: FuelTypeEnum
    extendedValueG: FuelTypeEnumExtensionTypeG | None = None
