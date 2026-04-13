"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .weight_type_enum import WeightTypeEnum
from .weight_type_enum_extension_type_g import WeightTypeEnumExtensionTypeG


@dataclass(kw_only=True)
class WeightTypeEnumGOutput:
    value: WeightTypeEnum
    extendedValueG: WeightTypeEnumExtensionTypeG | None = None
