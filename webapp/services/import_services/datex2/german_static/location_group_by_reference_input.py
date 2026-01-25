"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .extension_type_g_input import ExtensionTypeGInput
from .predefined_location_group_versioned_reference_g_input import PredefinedLocationGroupVersionedReferenceGInput


@validataclass
class LocationGroupByReferenceInput:
    predefinedLocationGroupReference: PredefinedLocationGroupVersionedReferenceGInput = DataclassValidator(
        PredefinedLocationGroupVersionedReferenceGInput
    )
    locLocationReferenceExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    locLocationGroupExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    locLocationGroupByReferenceExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
