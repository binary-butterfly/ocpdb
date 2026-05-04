"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator, FloatValidator, IntegerValidator

from .computation_method_enum_g_input import ComputationMethodEnumGInput
from .extension_type_g_input import ExtensionTypeGInput
from .multilingual_string_input import MultilingualStringInput


@validataclass
class PcuFlowValueInput(ValidataclassMixin):
    dataError: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    reasonForDataError: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    accuracy: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    computationalMethod: ComputationMethodEnumGInput | UnsetValueType = (
        DataclassValidator(ComputationMethodEnumGInput),
        Default(UnsetValue),
    )
    numberOfIncompleteInputs: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    numberOfInputValuesUsed: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    smoothingFactor: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    standardDeviation: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    supplierCalculatedDataQuality: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    pcuFlowRate: int = IntegerValidator(min_value=0)
    comDataValueExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    roaPcuFlowValueExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
