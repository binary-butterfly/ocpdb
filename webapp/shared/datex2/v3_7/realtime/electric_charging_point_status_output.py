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

from .duration_value_output import DurationValueOutput
from .energy_rate_update_output import EnergyRateUpdateOutput
from .fault_g_output import FaultGOutput
from .opening_status_enum_g_output import OpeningStatusEnumGOutput
from .operation_status_enum_g_output import OperationStatusEnumGOutput
from .planned_refill_point_status_output import PlannedRefillPointStatusOutput
from .refill_point_status_enum_g_output import RefillPointStatusEnumGOutput
from .supplemental_facility_status_output import SupplementalFacilityStatusOutput


@dataclass(kw_only=True)
class ElectricChargingPointStatusOutput:
    reference: FacilityObjectVersionedReferenceGOutput
    lastUpdated: datetime | None = None
    openingStatus: OpeningStatusEnumGOutput | None = None
    operationStatus: OperationStatusEnumGOutput | None = None
    regularOperatingHoursInForce: bool | None = None
    statusDescription: MultilingualStringOutput | None = None
    status: RefillPointStatusEnumGOutput
    unitsInStock: float | None = None
    remainingChargingTime: float | None = None
    currentVoltage: float | None = None
    currentChargingPower: float | None = None
    nextAvailableChargingSlots: list[datetime] | None = None
    newOperatingHours: OperatingHoursGOutput | None = None
    newRates: RatesGOutput | None = None
    fault: FaultGOutput | None = None
    supplementalFacilityStatus: list[SupplementalFacilityStatusOutput] | None = None
    energyRateUpdate: list[EnergyRateUpdateOutput] | None = None
    waitingTime: DurationValueOutput | None = None
    plannedRefillPointStatus: list[PlannedRefillPointStatusOutput] | None = None
    afacFacilityObjectStatusExtensionG: ExtensionTypeGOutput | None = None
    afacFacilityStatusExtensionG: ExtensionTypeGOutput | None = None
    aegiRefillPointStatusExtensionG: ExtensionTypeGOutput | None = None
    aegiElectricChargingPointStatusExtensionG: ExtensionTypeGOutput | None = None
