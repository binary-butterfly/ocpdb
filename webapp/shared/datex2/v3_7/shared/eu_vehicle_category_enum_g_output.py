"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .eu_vehicle_category_enum import EuVehicleCategoryEnum


@dataclass(kw_only=True)
class EuVehicleCategoryEnumGOutput:
    value: EuVehicleCategoryEnum
    extendedValueG: str | None = None
