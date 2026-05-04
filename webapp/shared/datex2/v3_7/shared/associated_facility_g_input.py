"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .associated_facility_input import AssociatedFacilityInput
from .associated_parking_input import AssociatedParkingInput


@validataclass
class AssociatedFacilityGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    afacAssociatedFacility: AssociatedFacilityInput | UnsetValueType = (
        DataclassValidator(AssociatedFacilityInput),
        Default(UnsetValue),
    )
    aegiAssociatedParking: AssociatedParkingInput | UnsetValueType = (
        DataclassValidator(AssociatedParkingInput),
        Default(UnsetValue),
    )
