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
    FloatValidator,
    IntegerValidator,
    ListValidator,
)

from .calculation_type_enum_g_input import CalculationTypeEnumGInput
from .extension_type_g_input import ExtensionTypeGInput


@validataclass
class DemandTypeInput(ValidataclassMixin):
    creationTime: datetime = DateTimeValidator()
    occupancyCalculation: list[CalculationTypeEnumGInput] = ListValidator(DataclassValidator(CalculationTypeEnumGInput))
    count: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    percentage: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    prkDemandTypeExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
