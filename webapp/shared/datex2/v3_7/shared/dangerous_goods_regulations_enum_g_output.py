"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .dangerous_goods_regulations_enum import DangerousGoodsRegulationsEnum


@dataclass(kw_only=True)
class DangerousGoodsRegulationsEnumGOutput:
    value: DangerousGoodsRegulationsEnum
    extendedValueG: str | None = None
