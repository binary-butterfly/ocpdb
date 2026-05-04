"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from datetime import datetime

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, DateTimeValidator, IntegerValidator, ListValidator

from .extension_type_g_input import ExtensionTypeGInput
from .facility_object_versioned_reference_g_input import FacilityObjectVersionedReferenceGInput
from .supply_view_type_enum_g_input import SupplyViewTypeEnumGInput


@validataclass
class SupplyInput(ValidataclassMixin):
    quantity: int = IntegerValidator()
    viewType: SupplyViewTypeEnumGInput = DataclassValidator(SupplyViewTypeEnumGInput)
    startValidUsagePeriod: datetime | UnsetValueType = DateTimeValidator(), Default(UnsetValue)
    endValidUsagePeriod: datetime | UnsetValueType = DateTimeValidator(), Default(UnsetValue)
    spacesReference: list[FacilityObjectVersionedReferenceGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(FacilityObjectVersionedReferenceGInput)),
        Default(UnsetValue),
    )
    prkSupplyExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
