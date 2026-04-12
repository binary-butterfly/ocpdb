"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .charging_mode_enum import ChargingModeEnum


@dataclass(kw_only=True)
class ChargingModeEnumGOutput:
    value: ChargingModeEnum
    extendedValueG: str | None = None
