"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, StringValidator

from .action_definition_versioned_reference_g_input import ActionDefinitionVersionedReferenceGInput
from .extension_type_g_input import ExtensionTypeGInput
from .measure_definition_versioned_reference_g_input import MeasureDefinitionVersionedReferenceGInput
from .strategy_definition_versioned_reference_g_input import StrategyDefinitionVersionedReferenceGInput


@validataclass
class TmplanImplementingActionInput(ValidataclassMixin):
    nonPredefinedActionIdReference: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    predefinedActionReference: ActionDefinitionVersionedReferenceGInput | UnsetValueType = (
        DataclassValidator(ActionDefinitionVersionedReferenceGInput),
        Default(UnsetValue),
    )
    predefinedMeasureReference: MeasureDefinitionVersionedReferenceGInput | UnsetValueType = (
        DataclassValidator(MeasureDefinitionVersionedReferenceGInput),
        Default(UnsetValue),
    )
    predefinedStrategyReference: StrategyDefinitionVersionedReferenceGInput | UnsetValueType = (
        DataclassValidator(StrategyDefinitionVersionedReferenceGInput),
        Default(UnsetValue),
    )
    tmpTmplanImplementingActionExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
