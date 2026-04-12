"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .electric_charging_equipment_output import ElectricChargingEquipmentOutput
from .supplemental_equipment_output import SupplementalEquipmentOutput
from .supplemental_service_facility_output import SupplementalServiceFacilityOutput


@dataclass(kw_only=True)
class SupplementalFacilityGOutput:
    """
    Only one of the properties shall be used in an instance.
    """

    afacSupplementalServiceFacility: SupplementalServiceFacilityOutput | None = None
    aegiElectricChargingEquipment: ElectricChargingEquipmentOutput | None = None
    afacSupplementalEquipment: SupplementalEquipmentOutput | None = None
