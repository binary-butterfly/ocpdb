"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .itinerary_by_indexed_locations_input import ItineraryByIndexedLocationsInput
from .itinerary_by_reference_input import ItineraryByReferenceInput


@validataclass
class ItineraryGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    locItineraryByIndexedLocations: ItineraryByIndexedLocationsInput | UnsetValueType = (
        DataclassValidator(ItineraryByIndexedLocationsInput),
        Default(UnsetValue),
    )
    locItineraryByReference: ItineraryByReferenceInput | UnsetValueType = (
        DataclassValidator(ItineraryByReferenceInput),
        Default(UnsetValue),
    )
