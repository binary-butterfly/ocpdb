"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .area_location_input import AreaLocationInput
from .location_by_reference_input import LocationByReferenceInput
from .point_location_input import PointLocationInput


@validataclass
class LocationGInput:
    locPointLocation: PointLocationInput | UnsetValueType = DataclassValidator(PointLocationInput), Default(UnsetValue)
    locLocationByReference: LocationByReferenceInput | UnsetValueType = (
        DataclassValidator(LocationByReferenceInput),
        Default(UnsetValue),
    )
    locAreaLocation: AreaLocationInput | UnsetValueType = DataclassValidator(AreaLocationInput), Default(UnsetValue)
