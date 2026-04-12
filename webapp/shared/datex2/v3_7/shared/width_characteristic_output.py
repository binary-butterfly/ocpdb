"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .comparison_operator_enum_g_output import ComparisonOperatorEnumGOutput
from .extension_type_g_output import ExtensionTypeGOutput


@dataclass(kw_only=True)
class WidthCharacteristicOutput:
    comparisonOperator: ComparisonOperatorEnumGOutput
    vehicleWidth: float
    comWidthCharacteristicExtensionG: ExtensionTypeGOutput | None = None
