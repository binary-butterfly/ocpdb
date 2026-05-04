"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from webapp.shared.datex2.v3_7.shared.area_location_input import AreaLocationInput
from webapp.shared.datex2.v3_7.shared.location_by_reference_input import LocationByReferenceInput

from .linear_location_input import LinearLocationInput
from .point_location_for_parking_input import PointLocationForParkingInput
from .point_location_input import PointLocationInput
from .single_road_linear_location_input import SingleRoadLinearLocationInput


@validataclass
class LocationGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

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
