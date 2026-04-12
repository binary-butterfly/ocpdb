"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .vehicle_characteristics_extended_output import VehicleCharacteristicsExtendedOutput


@dataclass(kw_only=True)
class VehicleCharacteristicsExtensionTypeGOutput:
    VehicleCharacteristicsExtended: VehicleCharacteristicsExtendedOutput | None = None
