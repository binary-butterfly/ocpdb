"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, FloatValidator

from .comparison_operator_enum_g_input import ComparisonOperatorEnumGInput
from .extension_type_g_input import ExtensionTypeGInput
from .power_unit_of_measure_enum_g_input import PowerUnitOfMeasureEnumGInput


@validataclass
class EnginePowerCharacteristicsInput(ValidataclassMixin):
    """
    Characteristics of the engine power of a vehicle.
    """

    comparisonOperator: ComparisonOperatorEnumGInput = DataclassValidator(ComparisonOperatorEnumGInput)
    enginePower: int = FloatValidator()
    unitOfMeasure: PowerUnitOfMeasureEnumGInput = DataclassValidator(PowerUnitOfMeasureEnumGInput)
    comxEnginePowerCharacteristicsExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
