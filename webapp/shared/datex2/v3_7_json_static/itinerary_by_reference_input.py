"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator

from .destination_g_input import DestinationGInput
from .extension_type_g_input import ExtensionTypeGInput
from .location_reference_extension_type_g_input import LocationReferenceExtensionTypeGInput
from .predefined_itinerary_versioned_reference_g_input import PredefinedItineraryVersionedReferenceGInput


@validataclass
class ItineraryByReferenceInput(ValidataclassMixin):
    """
    Multiple (i.e. more than one) physically separate locations which are ordered that constitute an itinerary or route where they are defined by reference to a predefined itinerary.
    """

    predefinedItineraryReference: PredefinedItineraryVersionedReferenceGInput = DataclassValidator(
        PredefinedItineraryVersionedReferenceGInput
    )
    routeDestination: list[DestinationGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(DestinationGInput)),
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
    locItineraryByReferenceExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
