"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .unit_of_speed_enum import UnitOfSpeedEnum


@dataclass(kw_only=True)
class UnitOfSpeedEnumGOutput:
    value: UnitOfSpeedEnum
    extendedValueG: str | None = None
