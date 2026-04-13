"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from webapp.shared.datex2.v3_7.shared.extension_type_g_output import ExtensionTypeGOutput
from webapp.shared.datex2.v3_7.shared.facility_object_versioned_reference_g_output import (
    FacilityObjectVersionedReferenceGOutput,
)
from webapp.shared.datex2.v3_7.shared.multilingual_string_output import MultilingualStringOutput

from .facility_type_enum_g_output import FacilityTypeEnumGOutput


@dataclass(kw_only=True)
class AssociatedParkingOutput:
    type: FacilityTypeEnumGOutput
    facilityReference: FacilityObjectVersionedReferenceGOutput | None = None
    description: MultilingualStringOutput | None = None
    carParkingCapacity: int | None = None
    truckParkingCapacity: int | None = None
    bikeParkingCapacity: int | None = None
    afacAssociatedFacilityExtensionG: ExtensionTypeGOutput | None = None
    aegiAssociatedParkingExtensionG: ExtensionTypeGOutput | None = None
