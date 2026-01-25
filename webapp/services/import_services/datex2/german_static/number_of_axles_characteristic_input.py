"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, IntegerValidator

from .comparison_operator_enum_g_input import ComparisonOperatorEnumGInput
from .extension_type_g_input import ExtensionTypeGInput


@validataclass
class NumberOfAxlesCharacteristicInput:
    comparisonOperator: ComparisonOperatorEnumGInput = DataclassValidator(ComparisonOperatorEnumGInput)
    numberOfAxles: int = IntegerValidator(min_value=0)
    comNumberOfAxlesCharacteristicExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
