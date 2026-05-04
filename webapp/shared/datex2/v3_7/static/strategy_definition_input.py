"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from datetime import datetime

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import (
    DataclassValidator,
    DateTimeValidator,
    IntegerValidator,
    ListValidator,
    StringValidator,
)

from webapp.shared.datex2.v3_7.shared.activation_conditions_input import ActivationConditionsInput
from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput
from webapp.shared.datex2.v3_7.shared.response_type_input import ResponseTypeInput

from .strategy_measure_input import StrategyMeasureInput


@validataclass
class StrategyDefinitionInput(ValidataclassMixin):
    idG: str = StringValidator()
    versionG: str = StringValidator()
    versionTime: datetime = DateTimeValidator()
    externalIdentification: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    description: MultilingualStringInput = DataclassValidator(MultilingualStringInput)
    shortName: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    priority: int | UnsetValueType = IntegerValidator(), Default(UnsetValue)
    strategyMeasure: list[StrategyMeasureInput] = ListValidator(DataclassValidator(StrategyMeasureInput))
    responseType: ResponseTypeInput | UnsetValueType = DataclassValidator(ResponseTypeInput), Default(UnsetValue)
    overallActivation: ActivationConditionsInput | UnsetValueType = (
        DataclassValidator(ActivationConditionsInput),
        Default(UnsetValue),
    )
    tmpStrategyExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    tmpStrategyDefinitionExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
