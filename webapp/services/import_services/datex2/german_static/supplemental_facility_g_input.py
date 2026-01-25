"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .electric_charging_equipment_input import ElectricChargingEquipmentInput
from .supplemental_equipment_input import SupplementalEquipmentInput
from .supplemental_service_facility_input import SupplementalServiceFacilityInput


@validataclass
class SupplementalFacilityGInput:
    afacSupplementalServiceFacility: SupplementalServiceFacilityInput | UnsetValueType = (
        DataclassValidator(SupplementalServiceFacilityInput),
        Default(UnsetValue),
    )
    afacSupplementalEquipment: SupplementalEquipmentInput | UnsetValueType = (
        DataclassValidator(SupplementalEquipmentInput),
        Default(UnsetValue),
    )
    aegiElectricChargingEquipment: ElectricChargingEquipmentInput | UnsetValueType = (
        DataclassValidator(ElectricChargingEquipmentInput),
        Default(UnsetValue),
    )
