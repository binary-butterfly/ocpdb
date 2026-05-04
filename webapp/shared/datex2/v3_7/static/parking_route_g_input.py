"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from webapp.shared.datex2.v3_7.shared.parking_route_by_reference_input import ParkingRouteByReferenceInput

from .parking_route_details_input import ParkingRouteDetailsInput


@validataclass
class ParkingRouteGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    prkParkingRouteDetails: ParkingRouteDetailsInput | UnsetValueType = (
        DataclassValidator(ParkingRouteDetailsInput),
        Default(UnsetValue),
    )
    prkParkingRouteByReference: ParkingRouteByReferenceInput | UnsetValueType = (
        DataclassValidator(ParkingRouteByReferenceInput),
        Default(UnsetValue),
    )
