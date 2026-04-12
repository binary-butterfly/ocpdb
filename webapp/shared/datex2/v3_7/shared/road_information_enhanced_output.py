"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .extension_type_g_output import ExtensionTypeGOutput
from .multilingual_string_output import MultilingualStringOutput
from .road_type_enum_g_output import RoadTypeEnumGOutput


@dataclass(kw_only=True)
class RoadInformationEnhancedOutput:
    roadDestination: str | None = None
    roadName: str | None = None
    roadNumber: str | None = None
    typeOfRoad: RoadTypeEnumGOutput | None = None
    roadOrigination: list[MultilingualStringOutput] | None = None
    locRoadInformationExtensionG: ExtensionTypeGOutput | None = None
    prkRoadInformationEnhancedExtensionG: ExtensionTypeGOutput | None = None
