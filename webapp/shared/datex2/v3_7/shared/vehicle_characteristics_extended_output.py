"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .age_characteristic_output import AgeCharacteristicOutput
from .engine_power_characteristics_output import EnginePowerCharacteristicsOutput
from .engine_type_enum_g_output import EngineTypeEnumGOutput
from .hazardous_materials_g_output import HazardousMaterialsGOutput
from .number_plate_characteristics_output import NumberPlateCharacteristicsOutput
from .numerical_emission_values_output import NumericalEmissionValuesOutput
from .owner_characteristic_output import OwnerCharacteristicOutput
from .regulated_characteristics_output import RegulatedCharacteristicsOutput
from .speed_output import SpeedOutput
from .trailer_characteristics_output import TrailerCharacteristicsOutput
from .vehicle_registration_characteristics_output import VehicleRegistrationCharacteristicsOutput


@dataclass(kw_only=True)
class VehicleCharacteristicsExtendedOutput:
    engineType: EngineTypeEnumGOutput | None = None
    ageCharacteristic: list[AgeCharacteristicOutput] | None = None
    maximumDesignSpeed: SpeedOutput | None = None
    trailerCharacteristics: TrailerCharacteristicsOutput | None = None
    hazardousMaterials: HazardousMaterialsGOutput | None = None
    ownerCharacteristic: OwnerCharacteristicOutput | None = None
    numberPlateCharacteristics: NumberPlateCharacteristicsOutput | None = None
    enginePowerCharacteristics: list[EnginePowerCharacteristicsOutput] | None = None
    numericalEmissionValues: list[NumericalEmissionValuesOutput] | None = None
    vehicleRegistrationCharacteristics: VehicleRegistrationCharacteristicsOutput | None = None
    regulatedCharacteristics: list[RegulatedCharacteristicsOutput] | None = None
