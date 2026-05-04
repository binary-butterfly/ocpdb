"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .access_status_input import AccessStatusInput
from .campus_status_input import CampusStatusInput
from .parking_status_information_input import ParkingStatusInformationInput
from .place_status_input import PlaceStatusInput
from .space_status_input import SpaceStatusInput


@validataclass
class ParkingStatusInformationGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    prkParkingStatusInformation: ParkingStatusInformationInput | UnsetValueType = (
        DataclassValidator(ParkingStatusInformationInput),
        Default(UnsetValue),
    )
    prkPlaceStatus: PlaceStatusInput | UnsetValueType = DataclassValidator(PlaceStatusInput), Default(UnsetValue)
    prkAccessStatus: AccessStatusInput | UnsetValueType = DataclassValidator(AccessStatusInput), Default(UnsetValue)
    prkCampusStatus: CampusStatusInput | UnsetValueType = DataclassValidator(CampusStatusInput), Default(UnsetValue)
    prkSpaceStatus: SpaceStatusInput | UnsetValueType = DataclassValidator(SpaceStatusInput), Default(UnsetValue)
