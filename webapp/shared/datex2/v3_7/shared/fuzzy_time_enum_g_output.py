"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .fuzzy_time_enum import FuzzyTimeEnum


@dataclass(kw_only=True)
class FuzzyTimeEnumGOutput:
    value: FuzzyTimeEnum
    extendedValueG: str | None = None
