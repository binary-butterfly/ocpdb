"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .altitude_confidence_output import AltitudeConfidenceOutput
from .extension_type_g_output import ExtensionTypeGOutput
from .height_type_enum_g_output import HeightTypeEnumGOutput
from .position_accuracy_output import PositionAccuracyOutput


@dataclass(kw_only=True)
class HeightCoordinateOutput:
    heightValue: float
    heightType: HeightTypeEnumGOutput | None = None
    altitudeConfidence: AltitudeConfidenceOutput | None = None
    verticalPositionAccuracy: PositionAccuracyOutput | None = None
    locHeightCoordinateExtensionG: ExtensionTypeGOutput | None = None
