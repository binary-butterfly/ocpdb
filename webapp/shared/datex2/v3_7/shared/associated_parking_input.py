"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, IntegerValidator

from .extension_type_g_input import ExtensionTypeGInput
from .facility_object_versioned_reference_g_input import FacilityObjectVersionedReferenceGInput
from .facility_type_enum_g_input import FacilityTypeEnumGInput
from .multilingual_string_input import MultilingualStringInput


@validataclass
class AssociatedParkingInput(ValidataclassMixin):
    type: FacilityTypeEnumGInput = DataclassValidator(FacilityTypeEnumGInput)
    facilityReference: FacilityObjectVersionedReferenceGInput | UnsetValueType = (
        DataclassValidator(FacilityObjectVersionedReferenceGInput),
        Default(UnsetValue),
    )
    description: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    carParkingCapacity: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    truckParkingCapacity: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    bikeParkingCapacity: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    afacAssociatedFacilityExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    aegiAssociatedParkingExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
