"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, FloatValidator

from .comparison_operator_enum_g_input import ComparisonOperatorEnumGInput
from .extension_type_g_input import ExtensionTypeGInput
from .weight_type_enum_g_input import WeightTypeEnumGInput


@validataclass
class GrossWeightCharacteristicInput:
    comparisonOperator: ComparisonOperatorEnumGInput = DataclassValidator(ComparisonOperatorEnumGInput)
    grossVehicleWeight: int = FloatValidator()
    typeOfWeight: WeightTypeEnumGInput = DataclassValidator(WeightTypeEnumGInput)
    comGrossWeightCharacteristicExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
