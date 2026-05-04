"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .available_spaces_thresholds_input import AvailableSpacesThresholdsInput
from .occupied_spaces_thresholds_input import OccupiedSpacesThresholdsInput
from .vehicles_on_site_thresholds_input import VehiclesOnSiteThresholdsInput


@validataclass
class ThresholdsGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    prkAvailableSpacesThresholds: AvailableSpacesThresholdsInput | UnsetValueType = (
        DataclassValidator(AvailableSpacesThresholdsInput),
        Default(UnsetValue),
    )
    prkVehiclesOnSiteThresholds: VehiclesOnSiteThresholdsInput | UnsetValueType = (
        DataclassValidator(VehiclesOnSiteThresholdsInput),
        Default(UnsetValue),
    )
    prkOccupiedSpacesThresholds: OccupiedSpacesThresholdsInput | UnsetValueType = (
        DataclassValidator(OccupiedSpacesThresholdsInput),
        Default(UnsetValue),
    )
