"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .eu_special_purpose_vehicle_enum import EuSpecialPurposeVehicleEnum


@dataclass(kw_only=True)
class EuSpecialPurposeVehicleEnumGOutput:
    value: EuSpecialPurposeVehicleEnum
    extendedValueG: str | None = None
