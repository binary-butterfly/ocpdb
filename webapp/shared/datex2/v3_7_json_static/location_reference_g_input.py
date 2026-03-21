"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .itinerary_by_indexed_locations_input import ItineraryByIndexedLocationsInput
from .itinerary_by_reference_input import ItineraryByReferenceInput
from .location_group_by_list_input import LocationGroupByListInput
from .location_group_by_reference_input import LocationGroupByReferenceInput
from .point_location_input import PointLocationInput


@validataclass
class LocationReferenceGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    locLocationGroupByList: LocationGroupByListInput | UnsetValueType = (
        DataclassValidator(LocationGroupByListInput),
        Default(UnsetValue),
    )
    locLocationGroupByReference: LocationGroupByReferenceInput | UnsetValueType = (
        DataclassValidator(LocationGroupByReferenceInput),
        Default(UnsetValue),
    )
    locItineraryByIndexedLocations: ItineraryByIndexedLocationsInput | UnsetValueType = (
        DataclassValidator(ItineraryByIndexedLocationsInput),
        Default(UnsetValue),
    )
    locItineraryByReference: ItineraryByReferenceInput | UnsetValueType = (
        DataclassValidator(ItineraryByReferenceInput),
        Default(UnsetValue),
    )
    locPointLocation: PointLocationInput | UnsetValueType = DataclassValidator(PointLocationInput), Default(UnsetValue)
