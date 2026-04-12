"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .comparison_operator_enum_g_output import ComparisonOperatorEnumGOutput
from .extension_type_g_output import ExtensionTypeGOutput
from .power_unit_of_measure_enum_g_output import PowerUnitOfMeasureEnumGOutput


@dataclass(kw_only=True)
class EnginePowerCharacteristicsOutput:
    comparisonOperator: ComparisonOperatorEnumGOutput
    enginePower: float
    unitOfMeasure: PowerUnitOfMeasureEnumGOutput
    comxEnginePowerCharacteristicsExtensionG: ExtensionTypeGOutput | None = None
