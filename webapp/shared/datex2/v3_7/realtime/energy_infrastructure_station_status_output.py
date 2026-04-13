"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass
from datetime import datetime

from webapp.shared.datex2.v3_7.shared.extension_type_g_output import ExtensionTypeGOutput
from webapp.shared.datex2.v3_7.shared.facility_object_versioned_reference_g_output import (
    FacilityObjectVersionedReferenceGOutput,
)
from webapp.shared.datex2.v3_7.shared.multilingual_string_output import MultilingualStringOutput
from webapp.shared.datex2.v3_7.shared.operating_hours_g_output import OperatingHoursGOutput
from webapp.shared.datex2.v3_7.shared.rates_g_output import RatesGOutput
from webapp.shared.datex2.v3_7.shared.service_type_output import ServiceTypeOutput

from .energy_rate_update_output import EnergyRateUpdateOutput
from .fault_g_output import FaultGOutput
from .opening_status_enum_g_output import OpeningStatusEnumGOutput
from .operation_status_enum_g_output import OperationStatusEnumGOutput
from .refill_point_status_g_output import RefillPointStatusGOutput
from .supplemental_facility_status_output import SupplementalFacilityStatusOutput


@dataclass(kw_only=True)
class EnergyInfrastructureStationStatusOutput:
    reference: FacilityObjectVersionedReferenceGOutput
    lastUpdated: datetime | None = None
    openingStatus: OpeningStatusEnumGOutput | None = None
    operationStatus: OperationStatusEnumGOutput | None = None
    regularOperatingHoursInForce: bool | None = None
    statusDescription: MultilingualStringOutput | None = None
    isAvailable: bool | None = None
    limitedHydrogenAmount: bool | None = None
    newOperatingHours: OperatingHoursGOutput | None = None
    newRates: RatesGOutput | None = None
    fault: FaultGOutput | None = None
    supplementalFacilityStatus: list[SupplementalFacilityStatusOutput] | None = None
    refillPointStatus: list[RefillPointStatusGOutput] | None = None
    serviceType: list[ServiceTypeOutput] | None = None
    energyRateUpdate: list[EnergyRateUpdateOutput] | None = None
    afacFacilityObjectStatusExtensionG: ExtensionTypeGOutput | None = None
    afacFacilityStatusExtensionG: ExtensionTypeGOutput | None = None
    aegiEnergyInfrastructureStationStatusExtensionG: ExtensionTypeGOutput | None = None
