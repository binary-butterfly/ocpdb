"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, FloatValidator, ListValidator

from webapp.shared.datex2.v3_7.shared.axle_characteristics_input import AxleCharacteristicsInput
from webapp.shared.datex2.v3_7.shared.computation_method_enum_g_input import ComputationMethodEnumGInput
from webapp.shared.datex2.v3_7.shared.direction_enum_g_input import DirectionEnumGInput
from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.lane_input import LaneInput
from webapp.shared.datex2.v3_7.shared.measured_or_derived_data_type_enum_g_input import (
    MeasuredOrDerivedDataTypeEnumGInput,
)

from .vehicle_characteristics_input import VehicleCharacteristicsInput


@validataclass
class MeasurementSpecificCharacteristicsInput(ValidataclassMixin):
    accuracy: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    computationMethod: ComputationMethodEnumGInput | UnsetValueType = (
        DataclassValidator(ComputationMethodEnumGInput),
        Default(UnsetValue),
    )
    defaultMeasurementHeight: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    measurementSide: DirectionEnumGInput | UnsetValueType = DataclassValidator(DirectionEnumGInput), Default(UnsetValue)
    period: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    smoothingFactor: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    specificMeasurementValueType: MeasuredOrDerivedDataTypeEnumGInput = DataclassValidator(
        MeasuredOrDerivedDataTypeEnumGInput
    )
    specificVehicleCharacteristics: VehicleCharacteristicsInput | UnsetValueType = (
        DataclassValidator(VehicleCharacteristicsInput),
        Default(UnsetValue),
    )
    specificLane: list[LaneInput] | UnsetValueType = ListValidator(DataclassValidator(LaneInput)), Default(UnsetValue)
    axleCharacteristics: AxleCharacteristicsInput | UnsetValueType = (
        DataclassValidator(AxleCharacteristicsInput),
        Default(UnsetValue),
    )
    roaMeasurementSpecificCharacteristicsExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
