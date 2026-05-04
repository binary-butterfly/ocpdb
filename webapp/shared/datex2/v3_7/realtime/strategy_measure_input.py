"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator, IntegerValidator

from webapp.shared.datex2.v3_7.shared.activation_conditions_input import ActivationConditionsInput
from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput

from .measure_g_input import MeasureGInput


@validataclass
class StrategyMeasureInput(ValidataclassMixin):
    processingIndex: int | UnsetValueType = IntegerValidator(), Default(UnsetValue)
    essentialForStrategy: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    activationConditions: ActivationConditionsInput | UnsetValueType = (
        DataclassValidator(ActivationConditionsInput),
        Default(UnsetValue),
    )
    measure: MeasureGInput = DataclassValidator(MeasureGInput)
    tmpStrategyMeasureExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
