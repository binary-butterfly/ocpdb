"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .price_type_enum import PriceTypeEnum


@dataclass(kw_only=True)
class PriceTypeEnumGOutput:
    value: PriceTypeEnum
    extendedValueG: str | None = None
