"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .refill_point_status_enum import RefillPointStatusEnum


@dataclass(kw_only=True)
class RefillPointStatusEnumGOutput:
    value: RefillPointStatusEnum
    extendedValueG: str | None = None
