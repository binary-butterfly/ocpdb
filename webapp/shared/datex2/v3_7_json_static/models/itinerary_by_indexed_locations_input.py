"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator

from .destination_g_input import DestinationGInput
from .extension_type_g_input import ExtensionTypeGInput
from .location_contained_in_itinerary_g_input import locationContainedInItineraryGInput
from .location_reference_extension_type_g_input import LocationReferenceExtensionTypeGInput


@validataclass
class ItineraryByIndexedLocationsInput(ValidataclassMixin):
    """
    Multiple physically separate locations arranged as an ordered set that defines an itinerary or route. The index qualifier indicates the order.
    """

    routeDestination: list[DestinationGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(DestinationGInput)),
        Default(UnsetValue),
    )
    locationContainedInItinerary: list[locationContainedInItineraryGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(locationContainedInItineraryGInput)),
        Default(UnsetValue),
    )
    locLocationReferenceExtensionG: LocationReferenceExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(LocationReferenceExtensionTypeGInput),
        Default(UnsetValue),
    )
    locItineraryExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    locItineraryByIndexedLocationsExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
