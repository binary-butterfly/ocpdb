"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .geographic_characteristic_enum import GeographicCharacteristicEnum


@dataclass(kw_only=True)
class GeographicCharacteristicEnumGOutput:
    value: GeographicCharacteristicEnum
    extendedValueG: str | None = None
