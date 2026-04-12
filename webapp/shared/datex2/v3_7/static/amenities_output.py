"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from webapp.shared.datex2.v3_7.shared.extension_type_g_output import ExtensionTypeGOutput


@dataclass(kw_only=True)
class AmenitiesOutput:
    illuminated: bool | None = None
    roofed: bool | None = None
    illuminatedRechargingParkingNearby: bool | None = None
    roofedRechargingParkingNearby: bool | None = None
    afacAmenitiesExtensionG: ExtensionTypeGOutput | None = None
