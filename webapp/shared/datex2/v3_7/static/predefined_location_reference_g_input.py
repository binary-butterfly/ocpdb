"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .predefined_itinerary_input import PredefinedItineraryInput
from .predefined_location_group_input import PredefinedLocationGroupInput
from .predefined_location_input import PredefinedLocationInput


@validataclass
class PredefinedLocationReferenceGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    locPredefinedLocationGroup: PredefinedLocationGroupInput | UnsetValueType = (
        DataclassValidator(PredefinedLocationGroupInput),
        Default(UnsetValue),
    )
    locPredefinedLocation: PredefinedLocationInput | UnsetValueType = (
        DataclassValidator(PredefinedLocationInput),
        Default(UnsetValue),
    )
    locPredefinedItinerary: PredefinedItineraryInput | UnsetValueType = (
        DataclassValidator(PredefinedItineraryInput),
        Default(UnsetValue),
    )
