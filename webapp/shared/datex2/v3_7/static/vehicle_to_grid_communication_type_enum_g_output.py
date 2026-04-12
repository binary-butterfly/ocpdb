"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .vehicle_to_grid_communication_type_enum import VehicleToGridCommunicationTypeEnum


@dataclass(kw_only=True)
class VehicleToGridCommunicationTypeEnumGOutput:
    value: VehicleToGridCommunicationTypeEnum
    extendedValueG: str | None = None
