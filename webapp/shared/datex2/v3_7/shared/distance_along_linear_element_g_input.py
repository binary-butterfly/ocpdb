"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .distance_from_linear_element_referent_input import DistanceFromLinearElementReferentInput
from .distance_from_linear_element_start_input import DistanceFromLinearElementStartInput
from .percentage_distance_along_linear_element_input import PercentageDistanceAlongLinearElementInput


@validataclass
class DistanceAlongLinearElementGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    locPercentageDistanceAlongLinearElement: PercentageDistanceAlongLinearElementInput | UnsetValueType = (
        DataclassValidator(PercentageDistanceAlongLinearElementInput),
        Default(UnsetValue),
    )
    locDistanceFromLinearElementReferent: DistanceFromLinearElementReferentInput | UnsetValueType = (
        DataclassValidator(DistanceFromLinearElementReferentInput),
        Default(UnsetValue),
    )
    locDistanceFromLinearElementStart: DistanceFromLinearElementStartInput | UnsetValueType = (
        DataclassValidator(DistanceFromLinearElementStartInput),
        Default(UnsetValue),
    )
