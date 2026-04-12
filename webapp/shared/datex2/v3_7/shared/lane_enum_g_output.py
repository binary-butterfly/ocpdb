"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .lane_enum import LaneEnum
from .lane_enum_extension_type_g import LaneEnumExtensionTypeG


@dataclass(kw_only=True)
class LaneEnumGOutput:
    value: LaneEnum
    extendedValueG: LaneEnumExtensionTypeG | None = None
