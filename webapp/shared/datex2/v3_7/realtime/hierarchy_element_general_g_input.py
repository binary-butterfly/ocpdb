"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .campus_input import CampusInput
from .pedestrian_access_input import PedestrianAccessInput
from .place_input import PlaceInput
from .space_input import SpaceInput
from .specific_area_input import SpecificAreaInput
from .subplace_element_input import SubplaceElementInput
from .supplemental_facility_input import SupplementalFacilityInput
from .vehicular_access_input import VehicularAccessInput


@validataclass
class HierarchyElementGeneralGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    prkSpace: SpaceInput | UnsetValueType = DataclassValidator(SpaceInput), Default(UnsetValue)
    prkSupplementalFacility: SupplementalFacilityInput | UnsetValueType = (
        DataclassValidator(SupplementalFacilityInput),
        Default(UnsetValue),
    )
    prkVehicularAccess: VehicularAccessInput | UnsetValueType = (
        DataclassValidator(VehicularAccessInput),
        Default(UnsetValue),
    )
    prkPedestrianAccess: PedestrianAccessInput | UnsetValueType = (
        DataclassValidator(PedestrianAccessInput),
        Default(UnsetValue),
    )
    prkSpecificArea: SpecificAreaInput | UnsetValueType = DataclassValidator(SpecificAreaInput), Default(UnsetValue)
    prkSubplaceElement: SubplaceElementInput | UnsetValueType = (
        DataclassValidator(SubplaceElementInput),
        Default(UnsetValue),
    )
    prkCampus: CampusInput | UnsetValueType = DataclassValidator(CampusInput), Default(UnsetValue)
    prkPlace: PlaceInput | UnsetValueType = DataclassValidator(PlaceInput), Default(UnsetValue)
