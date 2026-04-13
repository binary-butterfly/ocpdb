"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .reservation_type_enum import ReservationTypeEnum


@dataclass(kw_only=True)
class ReservationTypeEnumGOutput:
    value: ReservationTypeEnum
    extendedValueG: str | None = None
