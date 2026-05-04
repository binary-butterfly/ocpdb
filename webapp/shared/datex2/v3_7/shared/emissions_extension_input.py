"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import ValidataclassMixin, validataclass
from validataclass.validators import DataclassValidator

from .comparison_operator_enum_g_input import ComparisonOperatorEnumGInput


@validataclass
class EmissionsExtensionInput(ValidataclassMixin):
    comparisonOperator: ComparisonOperatorEnumGInput = DataclassValidator(ComparisonOperatorEnumGInput)
