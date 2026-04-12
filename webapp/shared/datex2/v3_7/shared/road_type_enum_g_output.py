"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .road_type_enum import RoadTypeEnum


@dataclass(kw_only=True)
class RoadTypeEnumGOutput:
    value: RoadTypeEnum
    extendedValueG: str | None = None
