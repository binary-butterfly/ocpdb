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
from webapp.shared.datex2.v3_7.shared.predefined_itinerary_versioned_reference_g_input import (
    PredefinedItineraryVersionedReferenceGInput,
)

from .destination_g_input import DestinationGInput


@validataclass
class ItineraryByReferenceInput(ValidataclassMixin):
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
