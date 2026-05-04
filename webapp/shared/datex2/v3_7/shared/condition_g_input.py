"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .condition_set_input import ConditionSetInput
from .trigger_condition_input import TriggerConditionInput


@validataclass
class ConditionGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    tmpTriggerCondition: TriggerConditionInput | UnsetValueType = (
        DataclassValidator(TriggerConditionInput),
        Default(UnsetValue),
    )
    tmpConditionSet: ConditionSetInput | UnsetValueType = DataclassValidator(ConditionSetInput), Default(UnsetValue)
