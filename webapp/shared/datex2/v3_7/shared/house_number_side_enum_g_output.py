"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .house_number_side_enum import HouseNumberSideEnum


@dataclass(kw_only=True)
class HouseNumberSideEnumGOutput:
    value: HouseNumberSideEnum
    extendedValueG: str | None = None
