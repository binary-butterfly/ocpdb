"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .confidentiality_value_enum import ConfidentialityValueEnum


@dataclass(kw_only=True)
class ConfidentialityValueEnumGOutput:
    value: ConfidentialityValueEnum
    extendedValueG: str | None = None
