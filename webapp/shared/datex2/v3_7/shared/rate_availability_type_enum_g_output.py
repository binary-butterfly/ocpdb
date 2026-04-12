"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .rate_availability_type_enum import RateAvailabilityTypeEnum


@dataclass(kw_only=True)
class RateAvailabilityTypeEnumGOutput:
    value: RateAvailabilityTypeEnum
    extendedValueG: str | None = None
