"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator, ListValidator, StringValidator

from .extension_type_g_input import ExtensionTypeGInput
from .facility_object_versioned_reference_g_input import FacilityObjectVersionedReferenceGInput
from .fault_input import FaultInput
from .multilingual_string_input import MultilingualStringInput
from .opening_status_enum_g_input import OpeningStatusEnumGInput
from .operating_hours_g_input import OperatingHoursGInput
from .operation_status_enum_g_input import OperationStatusEnumGInput
from .supplemental_facility_status_input import SupplementalFacilityStatusInput


@validataclass
class FacilityStatusInput(ValidataclassMixin):
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
    newOperatingHours: OperatingHoursGInput | UnsetValueType = (
        DataclassValidator(OperatingHoursGInput),
        Default(UnsetValue),
    )
    fault: FaultInput | UnsetValueType = DataclassValidator(FaultInput), Default(UnsetValue)
    supplementalFacilityStatus: list[SupplementalFacilityStatusInput] | UnsetValueType = (
        ListValidator(DataclassValidator(SupplementalFacilityStatusInput)),
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
