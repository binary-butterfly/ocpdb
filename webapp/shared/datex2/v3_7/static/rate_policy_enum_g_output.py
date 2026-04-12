"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .rate_policy_enum import RatePolicyEnum


@dataclass(kw_only=True)
class RatePolicyEnumGOutput:
    value: RatePolicyEnum
    extendedValueG: str | None = None
