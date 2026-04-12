"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .road_information_enhanced_output import RoadInformationEnhancedOutput
from .road_information_output import RoadInformationOutput


@dataclass(kw_only=True)
class RoadInformationGOutput:
    """
    Only one of the properties shall be used in an instance.
    """

    locRoadInformation: RoadInformationOutput | None = None
    prkRoadInformationEnhanced: RoadInformationEnhancedOutput | None = None
