"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator

from .activation_delay_input import ActivationDelayInput
from .condition_g_input import ConditionGInput
from .extension_type_g_input import ExtensionTypeGInput


@validataclass
class ActivationConditionsInput(ValidataclassMixin):
    automaticallyApproved: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    automaticallyImplemented: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    automaticallyDeactivated: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    activationDelay: ActivationDelayInput | UnsetValueType = (
        DataclassValidator(ActivationDelayInput),
        Default(UnsetValue),
    )
    activationTrigger: ConditionGInput | UnsetValueType = DataclassValidator(ConditionGInput), Default(UnsetValue)
    deactivationTrigger: ConditionGInput | UnsetValueType = DataclassValidator(ConditionGInput), Default(UnsetValue)
    tmpActivationConditionsExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
