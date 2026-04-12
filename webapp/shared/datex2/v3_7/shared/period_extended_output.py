"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .fuzzy_period_output import FuzzyPeriodOutput


@dataclass(kw_only=True)
class PeriodExtendedOutput:
    fuzzyPeriod: list[FuzzyPeriodOutput] | None = None
