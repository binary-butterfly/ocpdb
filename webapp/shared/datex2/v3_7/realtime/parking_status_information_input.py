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

from webapp.shared.datex2.v3_7.shared.demand_table_input import DemandTableInput
from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.facility_object_versioned_reference_g_input import (
    FacilityObjectVersionedReferenceGInput,
)
from webapp.shared.datex2.v3_7.shared.fault_g_input import FaultGInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput
from webapp.shared.datex2.v3_7.shared.opening_status_enum_g_input import OpeningStatusEnumGInput
from webapp.shared.datex2.v3_7.shared.operating_hours_g_input import OperatingHoursGInput
from webapp.shared.datex2.v3_7.shared.operating_pattern_status_input import OperatingPatternStatusInput
from webapp.shared.datex2.v3_7.shared.parking_conditions_enum_g_input import ParkingConditionsEnumGInput
from webapp.shared.datex2.v3_7.shared.parking_fault_enum_g_input import ParkingFaultEnumGInput
from webapp.shared.datex2.v3_7.shared.parking_route_status_input import ParkingRouteStatusInput
from webapp.shared.datex2.v3_7.shared.status_validity_g_input import StatusValidityGInput
from webapp.shared.datex2.v3_7.shared.supply_input import SupplyInput
from webapp.shared.datex2.v3_7.shared.winter_equipment_management_type_enum_g_input import (
    WinterEquipmentManagementTypeEnumGInput,
)

from .occupancy_input import OccupancyInput
from .rates_g_input import RatesGInput
from .supplemental_facility_status_input import SupplementalFacilityStatusInput


@validataclass
class ParkingStatusInformationInput(ValidataclassMixin):
    reference: FacilityObjectVersionedReferenceGInput = DataclassValidator(FacilityObjectVersionedReferenceGInput)
    lastUpdated: datetime | UnsetValueType = DateTimeValidator(), Default(UnsetValue)
    openingStatus: OpeningStatusEnumGInput | UnsetValueType = (
        DataclassValidator(OpeningStatusEnumGInput),
        Default(UnsetValue),
    )
    regularOperatingHoursInForce: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    statusDescription: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    queueingTime: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    parkingConditions: ParkingConditionsEnumGInput | UnsetValueType = (
        DataclassValidator(ParkingConditionsEnumGInput),
        Default(UnsetValue),
    )
    blurredAvailability: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    parkingFault: list[ParkingFaultEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(ParkingFaultEnumGInput)),
        Default(UnsetValue),
    )
    winterEquipmentManagementType: list[WinterEquipmentManagementTypeEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(WinterEquipmentManagementTypeEnumGInput)),
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
    parkingRouteStatus: list[ParkingRouteStatusInput] | UnsetValueType = (
        ListValidator(DataclassValidator(ParkingRouteStatusInput)),
        Default(UnsetValue),
    )
    occupancy: OccupancyInput | UnsetValueType = DataclassValidator(OccupancyInput), Default(UnsetValue)
    statusValidity: StatusValidityGInput | UnsetValueType = (
        DataclassValidator(StatusValidityGInput),
        Default(UnsetValue),
    )
    operatingPatternStatus: list[OperatingPatternStatusInput] | UnsetValueType = (
        ListValidator(DataclassValidator(OperatingPatternStatusInput)),
        Default(UnsetValue),
    )
    supply: SupplyInput | UnsetValueType = DataclassValidator(SupplyInput), Default(UnsetValue)
    demandTable: DemandTableInput | UnsetValueType = DataclassValidator(DemandTableInput), Default(UnsetValue)
    facFacilityObjectStatusExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    facFacilityStatusExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    prkParkingStatusInformationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
