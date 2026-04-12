"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .equipment_type_enum import EquipmentTypeEnum


@dataclass(kw_only=True)
class EquipmentTypeEnumGOutput:
    value: EquipmentTypeEnum
    extendedValueG: str | None = None
