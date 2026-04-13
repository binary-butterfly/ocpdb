"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .afir_facility_location_output import AfirFacilityLocationOutput


@dataclass(kw_only=True)
class LocationExtensionTypeGOutput:
    AfirFacilityLocation: AfirFacilityLocationOutput | None = None
