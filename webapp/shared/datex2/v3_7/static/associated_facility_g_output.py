"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .associated_facility_output import AssociatedFacilityOutput
from .associated_parking_output import AssociatedParkingOutput


@dataclass(kw_only=True)
class AssociatedFacilityGOutput:
    """
    Only one of the properties shall be used in an instance.
    """

    afacAssociatedFacility: AssociatedFacilityOutput | None = None
    aegiAssociatedParking: AssociatedParkingOutput | None = None
