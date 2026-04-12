"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .electric_charging_point_output import ElectricChargingPointOutput


@dataclass(kw_only=True)
class RefillPointGOutput:
    """
    Only one of the properties shall be used in an instance.
    """

    aegiElectricChargingPoint: ElectricChargingPointOutput | None = None
