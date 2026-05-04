"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator

from webapp.shared.datex2.v3_7.shared.age_characteristic_input import AgeCharacteristicInput
from webapp.shared.datex2.v3_7.shared.engine_power_characteristics_input import EnginePowerCharacteristicsInput
from webapp.shared.datex2.v3_7.shared.engine_type_enum_g_input import EngineTypeEnumGInput
from webapp.shared.datex2.v3_7.shared.hazardous_materials_g_input import HazardousMaterialsGInput
from webapp.shared.datex2.v3_7.shared.number_plate_characteristics_input import NumberPlateCharacteristicsInput
from webapp.shared.datex2.v3_7.shared.numerical_emission_values_input import NumericalEmissionValuesInput
from webapp.shared.datex2.v3_7.shared.regulated_characteristics_input import RegulatedCharacteristicsInput
from webapp.shared.datex2.v3_7.shared.speed_input import SpeedInput
from webapp.shared.datex2.v3_7.shared.trailer_characteristics_input import TrailerCharacteristicsInput
from webapp.shared.datex2.v3_7.shared.vehicle_registration_characteristics_input import (
    VehicleRegistrationCharacteristicsInput,
)

from .owner_characteristic_input import OwnerCharacteristicInput


@validataclass
class VehicleCharacteristicsExtendedInput(ValidataclassMixin):
    engineType: EngineTypeEnumGInput | UnsetValueType = DataclassValidator(EngineTypeEnumGInput), Default(UnsetValue)
    ageCharacteristic: list[AgeCharacteristicInput] | UnsetValueType = (
        ListValidator(DataclassValidator(AgeCharacteristicInput)),
        Default(UnsetValue),
    )
    maximumDesignSpeed: SpeedInput | UnsetValueType = DataclassValidator(SpeedInput), Default(UnsetValue)
    trailerCharacteristics: TrailerCharacteristicsInput | UnsetValueType = (
        DataclassValidator(TrailerCharacteristicsInput),
        Default(UnsetValue),
    )
    hazardousMaterials: HazardousMaterialsGInput | UnsetValueType = (
        DataclassValidator(HazardousMaterialsGInput),
        Default(UnsetValue),
    )
    ownerCharacteristic: OwnerCharacteristicInput | UnsetValueType = (
        DataclassValidator(OwnerCharacteristicInput),
        Default(UnsetValue),
    )
    numberPlateCharacteristics: NumberPlateCharacteristicsInput | UnsetValueType = (
        DataclassValidator(NumberPlateCharacteristicsInput),
        Default(UnsetValue),
    )
    enginePowerCharacteristics: list[EnginePowerCharacteristicsInput] | UnsetValueType = (
        ListValidator(DataclassValidator(EnginePowerCharacteristicsInput)),
        Default(UnsetValue),
    )
    numericalEmissionValues: list[NumericalEmissionValuesInput] | UnsetValueType = (
        ListValidator(DataclassValidator(NumericalEmissionValuesInput)),
        Default(UnsetValue),
    )
    vehicleRegistrationCharacteristics: VehicleRegistrationCharacteristicsInput | UnsetValueType = (
        DataclassValidator(VehicleRegistrationCharacteristicsInput),
        Default(UnsetValue),
    )
    regulatedCharacteristics: list[RegulatedCharacteristicsInput] | UnsetValueType = (
        ListValidator(DataclassValidator(RegulatedCharacteristicsInput)),
        Default(UnsetValue),
    )
