"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .comparison_operator_enum_g_output import ComparisonOperatorEnumGOutput
from .extension_type_g_output import ExtensionTypeGOutput
from .non_negative_integer_comparison_output import NonNegativeIntegerComparisonOutput


@dataclass(kw_only=True)
class AgeCharacteristicOutput:
    comparisonOperator: ComparisonOperatorEnumGOutput
    yearOfFirstRegistration: int | None = None
    yearOfLastRegistration: int | None = None
    vehicleAge: NonNegativeIntegerComparisonOutput | None = None
    comxAgeCharacteristicExtensionG: ExtensionTypeGOutput | None = None
