"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .controlled_zone_activation_input import ControlledZoneActivationInput
from .non_predefined_condition_activation_input import NonPredefinedConditionActivationInput
from .predefined_condition_activation_input import PredefinedConditionActivationInput
from .traffic_regulation_activation_input import TrafficRegulationActivationInput


@validataclass
class ActivationStatusGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    czPredefinedConditionActivation: PredefinedConditionActivationInput | UnsetValueType = (
        DataclassValidator(PredefinedConditionActivationInput),
        Default(UnsetValue),
    )
    czNonPredefinedConditionActivation: NonPredefinedConditionActivationInput | UnsetValueType = (
        DataclassValidator(NonPredefinedConditionActivationInput),
        Default(UnsetValue),
    )
    czTrafficRegulationActivation: TrafficRegulationActivationInput | UnsetValueType = (
        DataclassValidator(TrafficRegulationActivationInput),
        Default(UnsetValue),
    )
    czControlledZoneActivation: ControlledZoneActivationInput | UnsetValueType = (
        DataclassValidator(ControlledZoneActivationInput),
        Default(UnsetValue),
    )
