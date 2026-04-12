"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .electric_charging_point_status_output import ElectricChargingPointStatusOutput
from .refill_point_status_output import RefillPointStatusOutput


@dataclass(kw_only=True)
class RefillPointStatusGOutput:
    """
    Only one of the properties shall be used in an instance.
    """

    aegiRefillPointStatus: RefillPointStatusOutput | None = None
    aegiElectricChargingPointStatus: ElectricChargingPointStatusOutput | None = None
