"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, FloatValidator

from .comparison_operator_enum_g_input import ComparisonOperatorEnumGInput
from .emission_type_enum_g_input import EmissionTypeEnumGInput
from .extension_type_g_input import ExtensionTypeGInput


@validataclass
class NumericalEmissionValuesInput(ValidataclassMixin):
    emissionType: EmissionTypeEnumGInput | UnsetValueType = (
        DataclassValidator(EmissionTypeEnumGInput),
        Default(UnsetValue),
    )
    value: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    comparisonOperator: ComparisonOperatorEnumGInput | UnsetValueType = (
        DataclassValidator(ComparisonOperatorEnumGInput),
        Default(UnsetValue),
    )
    comxNumericalEmissionValuesExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
