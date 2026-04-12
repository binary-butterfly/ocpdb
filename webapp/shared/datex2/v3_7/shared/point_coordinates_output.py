"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .extension_type_g_output import ExtensionTypeGOutput
from .height_coordinate_output import HeightCoordinateOutput
from .position_accuracy_output import PositionAccuracyOutput
from .position_confidence_ellipse_output import PositionConfidenceEllipseOutput


@dataclass(kw_only=True)
class PointCoordinatesOutput:
    latitude: float
    longitude: float
    heightCoordinate: list[HeightCoordinateOutput] | None = None
    positionConfidenceEllipse: PositionConfidenceEllipseOutput | None = None
    horizontalPositionAccuracy: PositionAccuracyOutput | None = None
    locPointCoordinatesExtensionG: ExtensionTypeGOutput | None = None
