"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from datetime import datetime

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, DateTimeValidator

from .extension_type_g_input import ExtensionTypeGInput
from .strategy_definition_versioned_reference_g_input import StrategyDefinitionVersionedReferenceGInput


@validataclass
class StrategyByReferenceInput(ValidataclassMixin):
    versionTime: datetime = DateTimeValidator()
    strategyReference: StrategyDefinitionVersionedReferenceGInput = DataclassValidator(
        StrategyDefinitionVersionedReferenceGInput
    )
    tmpStrategyExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    tmpStrategyByReferenceExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
