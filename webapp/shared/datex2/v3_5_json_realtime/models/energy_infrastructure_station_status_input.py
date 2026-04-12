"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from datetime import datetime

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator, DateTimeValidator, ListValidator

from .energy_rate_update_input import EnergyRateUpdateInput
from .extension_type_g_input import ExtensionTypeGInput
from .facility_object_versioned_reference_g_input import FacilityObjectVersionedReferenceGInput
from .fault_input import FaultInput
from .multilingual_string_input import MultilingualStringInput
from .opening_status_enum_g_input import OpeningStatusEnumGInput
from .operating_hours_g_input import OperatingHoursGInput
from .operation_status_enum_g_input import OperationStatusEnumGInput
from .refill_point_status_g_input import RefillPointStatusGInput
from .service_type_input import ServiceTypeInput
from .supplemental_facility_status_input import SupplementalFacilityStatusInput


@validataclass
class EnergyInfrastructureStationStatusInput(ValidataclassMixin):
    """
    Dynamic information on the status of the station.
    """

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
    isAvailable: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    newOperatingHours: OperatingHoursGInput | UnsetValueType = (
        DataclassValidator(OperatingHoursGInput),
        Default(UnsetValue),
    )
    fault: FaultInput | UnsetValueType = DataclassValidator(FaultInput), Default(UnsetValue)
    supplementalFacilityStatus: list[SupplementalFacilityStatusInput] | UnsetValueType = (
        ListValidator(DataclassValidator(SupplementalFacilityStatusInput)),
        Default(UnsetValue),
    )
    refillPointStatus: list[RefillPointStatusGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(RefillPointStatusGInput)),
        Default(UnsetValue),
    )
    serviceType: list[ServiceTypeInput] | UnsetValueType = (
        ListValidator(DataclassValidator(ServiceTypeInput)),
        Default(UnsetValue),
    )
    energyRateUpdate: list[EnergyRateUpdateInput] | UnsetValueType = (
        ListValidator(DataclassValidator(EnergyRateUpdateInput)),
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
    aegiEnergyInfrastructureStationStatusExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
