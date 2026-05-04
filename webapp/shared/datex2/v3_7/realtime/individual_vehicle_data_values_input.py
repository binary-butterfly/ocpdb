"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from datetime import datetime

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, DateTimeValidator, FloatValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.measurement_or_calculation_time_input import MeasurementOrCalculationTimeInput

from .vehicle_characteristics_input import VehicleCharacteristicsInput
from .vehicle_input import VehicleInput


@validataclass
class IndividualVehicleDataValuesInput(ValidataclassMixin):
    arrivalTime: datetime | UnsetValueType = DateTimeValidator(), Default(UnsetValue)
    distanceGap: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    distanceHeadway: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    exitTime: datetime | UnsetValueType = DateTimeValidator(), Default(UnsetValue)
    passageDuration: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    presenceDuration: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    speed: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    timeGap: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    timeHeadway: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    measurementOrCalculationTime: MeasurementOrCalculationTimeInput | UnsetValueType = (
        DataclassValidator(MeasurementOrCalculationTimeInput),
        Default(UnsetValue),
    )
    forVehiclesWithCharacteristicsOf: VehicleCharacteristicsInput | UnsetValueType = (
        DataclassValidator(VehicleCharacteristicsInput),
        Default(UnsetValue),
    )
    individualVehicle: VehicleInput | UnsetValueType = DataclassValidator(VehicleInput), Default(UnsetValue)
    roaBasicDataExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    roaTrafficDataExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    roaIndividualVehicleDataValuesExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
