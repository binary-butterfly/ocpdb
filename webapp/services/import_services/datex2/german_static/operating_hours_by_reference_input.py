"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .closure_information_input import ClosureInformationInput
from .extension_type_g_input import ExtensionTypeGInput
from .operating_hours_specification_versioned_reference_g_input import (
    OperatingHoursSpecificationVersionedReferenceGInput,
)
from .operating_hours_table_versioned_reference_g_input import OperatingHoursTableVersionedReferenceGInput


@validataclass
class OperatingHoursByReferenceInput:
    operatingHoursReference: OperatingHoursSpecificationVersionedReferenceGInput = DataclassValidator(
        OperatingHoursSpecificationVersionedReferenceGInput
    )
    operatingHoursTableReference: OperatingHoursTableVersionedReferenceGInput | UnsetValueType = (
        DataclassValidator(OperatingHoursTableVersionedReferenceGInput),
        Default(UnsetValue),
    )
    closureInformation: ClosureInformationInput | UnsetValueType = (
        DataclassValidator(ClosureInformationInput),
        Default(UnsetValue),
    )
    afacOperatingHoursExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    afacOperatingHoursByReferenceExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
