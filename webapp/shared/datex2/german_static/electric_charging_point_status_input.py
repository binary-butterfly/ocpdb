"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import (
    BooleanValidator,
    DataclassValidator,
    FloatValidator,
    ListValidator,
    StringValidator,
)

from .duration_value_input import DurationValueInput
from .energy_rate_update_input import EnergyRateUpdateInput
from .extension_type_g_input import ExtensionTypeGInput
from .facility_object_versioned_reference_g_input import FacilityObjectVersionedReferenceGInput
from .fault_input import FaultInput
from .multilingual_string_input import MultilingualStringInput
from .opening_status_enum_g_input import OpeningStatusEnumGInput
from .operating_hours_g_input import OperatingHoursGInput
from .operation_status_enum_g_input import OperationStatusEnumGInput
from .planned_refill_point_status_input import PlannedRefillPointStatusInput
from .refill_point_status_enum_g_input import RefillPointStatusEnumGInput
from .supplemental_facility_status_input import SupplementalFacilityStatusInput


@validataclass
class ElectricChargingPointStatusInput(ValidataclassMixin):
    reference: FacilityObjectVersionedReferenceGInput = DataclassValidator(FacilityObjectVersionedReferenceGInput)
    lastUpdated: str | UnsetValueType = StringValidator(), Default(UnsetValue)
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
    unitsInStock: int | UnsetValueType = FloatValidator(), Default(UnsetValue)
    remainingChargingTime: int | UnsetValueType = FloatValidator(), Default(UnsetValue)
    currentVoltage: int | UnsetValueType = FloatValidator(), Default(UnsetValue)
    currentChargingPower: int | UnsetValueType = FloatValidator(), Default(UnsetValue)
    nextAvailableChargingSlots: list[str] | UnsetValueType = ListValidator(StringValidator()), Default(UnsetValue)
    newOperatingHours: OperatingHoursGInput | UnsetValueType = (
        DataclassValidator(OperatingHoursGInput),
        Default(UnsetValue),
    )
    fault: FaultInput | UnsetValueType = DataclassValidator(FaultInput), Default(UnsetValue)
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
