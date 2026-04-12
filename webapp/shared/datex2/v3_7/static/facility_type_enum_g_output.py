"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .facility_type_enum import FacilityTypeEnum


@dataclass(kw_only=True)
class FacilityTypeEnumGOutput:
    value: FacilityTypeEnum
    extendedValueG: str | None = None
