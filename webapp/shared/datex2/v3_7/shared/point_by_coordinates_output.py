"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .extension_type_g_output import ExtensionTypeGOutput
from .point_coordinates_output import PointCoordinatesOutput


@dataclass(kw_only=True)
class PointByCoordinatesOutput:
    bearing: int | None = None
    pointCoordinates: PointCoordinatesOutput
    locPointByCoordinatesExtensionG: ExtensionTypeGOutput | None = None
