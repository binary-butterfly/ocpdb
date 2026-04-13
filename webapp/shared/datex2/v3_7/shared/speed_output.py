"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .extension_type_g_output import ExtensionTypeGOutput
from .unit_of_speed_enum_g_output import UnitOfSpeedEnumGOutput


@dataclass(kw_only=True)
class SpeedOutput:
    numericValue: float
    unitOfMeasure: UnitOfSpeedEnumGOutput
    comxSpeedExtensionG: ExtensionTypeGOutput | None = None
