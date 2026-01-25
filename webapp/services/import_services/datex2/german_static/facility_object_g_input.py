"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .dedicated_parking_spaces_input import DedicatedParkingSpacesInput
from .electric_charging_equipment_input import ElectricChargingEquipmentInput
from .electric_charging_point_input import ElectricChargingPointInput
from .energy_infrastructure_site_input import EnergyInfrastructureSiteInput
from .energy_infrastructure_station_input import EnergyInfrastructureStationInput
from .supplemental_equipment_input import SupplementalEquipmentInput
from .supplemental_service_facility_input import SupplementalServiceFacilityInput


@validataclass
class FacilityObjectGInput:
    aegiDedicatedParkingSpaces: DedicatedParkingSpacesInput | UnsetValueType = (
        DataclassValidator(DedicatedParkingSpacesInput),
        Default(UnsetValue),
    )
    aegiElectricChargingPoint: ElectricChargingPointInput | UnsetValueType = (
        DataclassValidator(ElectricChargingPointInput),
        Default(UnsetValue),
    )
    aegiEnergyInfrastructureStation: EnergyInfrastructureStationInput | UnsetValueType = (
        DataclassValidator(EnergyInfrastructureStationInput),
        Default(UnsetValue),
    )
    aegiEnergyInfrastructureSite: EnergyInfrastructureSiteInput | UnsetValueType = (
        DataclassValidator(EnergyInfrastructureSiteInput),
        Default(UnsetValue),
    )
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
