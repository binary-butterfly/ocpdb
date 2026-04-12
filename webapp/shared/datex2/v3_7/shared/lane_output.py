"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .extension_type_g_output import ExtensionTypeGOutput
from .lane_enum_g_output import LaneEnumGOutput


@dataclass(kw_only=True)
class LaneOutput:
    laneNumber: int | None = None
    laneUsage: LaneEnumGOutput | None = None
    locLaneExtensionG: ExtensionTypeGOutput | None = None
