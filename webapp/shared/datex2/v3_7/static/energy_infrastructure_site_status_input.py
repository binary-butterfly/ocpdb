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
    IntegerValidator,
    ListValidator,
)

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.facility_object_versioned_reference_g_input import (
    FacilityObjectVersionedReferenceGInput,
)
from webapp.shared.datex2.v3_7.shared.fault_g_input import FaultGInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput
from webapp.shared.datex2.v3_7.shared.opening_status_enum_g_input import OpeningStatusEnumGInput
from webapp.shared.datex2.v3_7.shared.operating_hours_g_input import OperatingHoursGInput
from webapp.shared.datex2.v3_7.shared.operation_status_enum_g_input import OperationStatusEnumGInput
from webapp.shared.datex2.v3_7.shared.service_type_input import ServiceTypeInput

from .energy_infrastructure_station_status_input import EnergyInfrastructureStationStatusInput
from .rates_g_input import RatesGInput
from .supplemental_facility_status_input import SupplementalFacilityStatusInput


@validataclass
class EnergyInfrastructureSiteStatusInput(ValidataclassMixin):
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
    availableCarParkingPlaces: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    availableTruckParkingPlaces: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
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
    energyInfrastructureStationStatus: list[EnergyInfrastructureStationStatusInput] | UnsetValueType = (
        ListValidator(DataclassValidator(EnergyInfrastructureStationStatusInput)),
        Default(UnsetValue),
    )
    serviceType: list[ServiceTypeInput] | UnsetValueType = (
        ListValidator(DataclassValidator(ServiceTypeInput)),
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
    aegiEnergyInfrastructureSiteStatusExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
