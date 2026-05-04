"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from webapp.shared.datex2.v3_7.shared.area_location_input import AreaLocationInput
from webapp.shared.datex2.v3_7.shared.location_by_reference_input import LocationByReferenceInput
from webapp.shared.datex2.v3_7.shared.location_group_by_reference_input import LocationGroupByReferenceInput

from .itinerary_by_indexed_locations_input import ItineraryByIndexedLocationsInput
from .itinerary_by_reference_input import ItineraryByReferenceInput
from .linear_location_input import LinearLocationInput
from .location_group_by_list_input import LocationGroupByListInput
from .point_location_for_parking_input import PointLocationForParkingInput
from .point_location_input import PointLocationInput
from .single_road_linear_location_input import SingleRoadLinearLocationInput


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
    locLinearLocation: LinearLocationInput | UnsetValueType = (
        DataclassValidator(LinearLocationInput),
        Default(UnsetValue),
    )
    locSingleRoadLinearLocation: SingleRoadLinearLocationInput | UnsetValueType = (
        DataclassValidator(SingleRoadLinearLocationInput),
        Default(UnsetValue),
    )
    locPointLocation: PointLocationInput | UnsetValueType = DataclassValidator(PointLocationInput), Default(UnsetValue)
    prkPointLocationForParking: PointLocationForParkingInput | UnsetValueType = (
        DataclassValidator(PointLocationForParkingInput),
        Default(UnsetValue),
    )
    locLocationByReference: LocationByReferenceInput | UnsetValueType = (
        DataclassValidator(LocationByReferenceInput),
        Default(UnsetValue),
    )
    locAreaLocation: AreaLocationInput | UnsetValueType = DataclassValidator(AreaLocationInput), Default(UnsetValue)
