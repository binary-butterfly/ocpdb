"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from datetime import datetime

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import (
    BooleanValidator,
    DataclassValidator,
    DateTimeValidator,
    FloatValidator,
    ListValidator,
)

from webapp.shared.datex2.v3_7.shared.duration_value_input import DurationValueInput
from webapp.shared.datex2.v3_7.shared.energy_rate_update_input import EnergyRateUpdateInput
from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.facility_object_versioned_reference_g_input import (
    FacilityObjectVersionedReferenceGInput,
)
from webapp.shared.datex2.v3_7.shared.fault_g_input import FaultGInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput
from webapp.shared.datex2.v3_7.shared.opening_status_enum_g_input import OpeningStatusEnumGInput
from webapp.shared.datex2.v3_7.shared.operating_hours_g_input import OperatingHoursGInput
from webapp.shared.datex2.v3_7.shared.operation_status_enum_g_input import OperationStatusEnumGInput
from webapp.shared.datex2.v3_7.shared.planned_refill_point_status_input import PlannedRefillPointStatusInput
from webapp.shared.datex2.v3_7.shared.refill_point_status_enum_g_input import RefillPointStatusEnumGInput

from .rates_g_input import RatesGInput
from .supplemental_facility_status_input import SupplementalFacilityStatusInput


@validataclass
class ElectricChargingPointStatusInput(ValidataclassMixin):
    reference: FacilityObjectVersionedReferenceGInput = DataclassValidator(FacilityObjectVersionedReferenceGInput)
    lastUpdated: datetime | UnsetValueType = DateTimeValidator(), Default(UnsetValue)
    openingStatus: OpeningStatusEnumGInput | UnsetValueType = (
        DataclassValidator(OpeningStatusEnumGInput),
        Default(UnsetValue),
    )
    operationStatus: OperationStatusEnumGInput | UnsetValueType = (
        DataclassValidator(OperationStatusEnumGInput),
        Default(UnsetValue),
    )
    regularOperatingHoursInForce: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    statusDescription: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    status: RefillPointStatusEnumGInput = DataclassValidator(RefillPointStatusEnumGInput)
    unitsInStock: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    remainingChargingTime: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    currentVoltage: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    currentChargingPower: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    nextAvailableChargingSlots: list[datetime] | UnsetValueType = (
        ListValidator(DateTimeValidator()),
        Default(UnsetValue),
    )
    newOperatingHours: OperatingHoursGInput | UnsetValueType = (
        DataclassValidator(OperatingHoursGInput),
        Default(UnsetValue),
    )
    newRates: RatesGInput | UnsetValueType = DataclassValidator(RatesGInput), Default(UnsetValue)
    fault: FaultGInput | UnsetValueType = DataclassValidator(FaultGInput), Default(UnsetValue)
    supplementalFacilityStatus: list[SupplementalFacilityStatusInput] | UnsetValueType = (
        ListValidator(DataclassValidator(SupplementalFacilityStatusInput)),
        Default(UnsetValue),
    )
    energyRateUpdate: list[EnergyRateUpdateInput] | UnsetValueType = (
        ListValidator(DataclassValidator(EnergyRateUpdateInput)),
        Default(UnsetValue),
    )
    waitingTime: DurationValueInput | UnsetValueType = DataclassValidator(DurationValueInput), Default(UnsetValue)
    plannedRefillPointStatus: list[PlannedRefillPointStatusInput] | UnsetValueType = (
        ListValidator(DataclassValidator(PlannedRefillPointStatusInput)),
        Default(UnsetValue),
    )
    afacFacilityObjectStatusExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    afacFacilityStatusExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    aegiRefillPointStatusExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    aegiElectricChargingPointStatusExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
