"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.location_reference_extension_type_g_input import (
    LocationReferenceExtensionTypeGInput,
)

from .location_g_input import LocationGInput


@validataclass
class LocationGroupByListInput(ValidataclassMixin):
    locationContainedInGroup: list[LocationGInput] = ListValidator(DataclassValidator(LocationGInput))
    locLocationReferenceExtensionG: LocationReferenceExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(LocationReferenceExtensionTypeGInput),
        Default(UnsetValue),
    )
    locLocationGroupExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    locLocationGroupByListExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
