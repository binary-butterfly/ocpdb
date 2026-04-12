"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .comparison_operator_enum import ComparisonOperatorEnum


@dataclass(kw_only=True)
class ComparisonOperatorEnumGOutput:
    value: ComparisonOperatorEnum
    extendedValueG: str | None = None
