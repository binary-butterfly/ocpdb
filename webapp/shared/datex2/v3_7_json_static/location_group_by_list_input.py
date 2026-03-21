"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator

from .extension_type_g_input import ExtensionTypeGInput
from .location_g_input import LocationGInput
from .location_reference_extension_type_g_input import LocationReferenceExtensionTypeGInput


@validataclass
class LocationGroupByListInput(ValidataclassMixin):
    """
    A group of (i.e. more than one) physically separate locations which have no specific order and where each location is explicitly listed.
    """

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
