"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .road_information_enhanced_input import RoadInformationEnhancedInput
from .road_information_input import RoadInformationInput


@validataclass
class RoadInformationGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    locRoadInformation: RoadInformationInput | UnsetValueType = (
        DataclassValidator(RoadInformationInput),
        Default(UnsetValue),
    )
    prkRoadInformationEnhanced: RoadInformationEnhancedInput | UnsetValueType = (
        DataclassValidator(RoadInformationEnhancedInput),
        Default(UnsetValue),
    )
