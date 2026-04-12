"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .charging_point_usage_type_enum import ChargingPointUsageTypeEnum


@dataclass(kw_only=True)
class ChargingPointUsageTypeEnumGOutput:
    value: ChargingPointUsageTypeEnum
    extendedValueG: str | None = None
