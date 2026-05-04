"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from webapp.shared.datex2.v3_7.shared.strategy_by_reference_input import StrategyByReferenceInput

from .strategy_definition_input import StrategyDefinitionInput


@validataclass
class StrategyGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    tmpStrategyByReference: StrategyByReferenceInput | UnsetValueType = (
        DataclassValidator(StrategyByReferenceInput),
        Default(UnsetValue),
    )
    tmpStrategyDefinition: StrategyDefinitionInput | UnsetValueType = (
        DataclassValidator(StrategyDefinitionInput),
        Default(UnsetValue),
    )
