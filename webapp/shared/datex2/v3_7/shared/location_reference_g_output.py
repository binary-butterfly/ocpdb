"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .point_location_output import PointLocationOutput


@dataclass(kw_only=True)
class LocationReferenceGOutput:
    """
    Only one of the properties shall be used in an instance.
    """

    locPointLocation: PointLocationOutput | None = None
