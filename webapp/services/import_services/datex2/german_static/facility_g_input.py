"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .electric_charging_point_input import ElectricChargingPointInput
from .energy_infrastructure_site_input import EnergyInfrastructureSiteInput
from .energy_infrastructure_station_input import EnergyInfrastructureStationInput


@validataclass
class FacilityGInput:
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
