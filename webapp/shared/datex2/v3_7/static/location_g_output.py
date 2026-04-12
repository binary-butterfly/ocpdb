"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from webapp.shared.datex2.v3_7.shared.point_location_output import PointLocationOutput


@dataclass(kw_only=True)
class LocationGOutput:
    """
    Only one of the properties shall be used in an instance.
    """

    locPointLocation: PointLocationOutput | None = None
