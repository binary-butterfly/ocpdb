"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import (
    BooleanValidator,
    DataclassValidator,
    FloatValidator,
    IntegerValidator,
    ListValidator,
)

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.parking_occupancy_enum_g_input import ParkingOccupancyEnumGInput
from webapp.shared.datex2.v3_7.shared.parking_occupancy_trend_enum_g_input import ParkingOccupancyTrendEnumGInput
from webapp.shared.datex2.v3_7.shared.parking_vacant_spaces_enum_g_input import ParkingVacantSpacesEnumGInput
from webapp.shared.datex2.v3_7.shared.percentage_value_input import PercentageValueInput
from webapp.shared.datex2.v3_7.shared.threshold_configuration_input import ThresholdConfigurationInput

from .vehicle_count_and_rate_input import VehicleCountAndRateInput


@validataclass
class OccupancyInput(ValidataclassMixin):
    numberOfSpacesOverride: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    numberOfVacantSpaces: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    numberOfVacantSpacesLowerThan: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    numberOfVacantSpacesHigherThan: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    numberOfVacantSpacesGraded: ParkingVacantSpacesEnumGInput | UnsetValueType = (
        DataclassValidator(ParkingVacantSpacesEnumGInput),
        Default(UnsetValue),
    )
    numberOfOccupiedSpaces: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    numberOfVehicles: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    occupancy: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    occupancyGraded: ParkingOccupancyEnumGInput | UnsetValueType = (
        DataclassValidator(ParkingOccupancyEnumGInput),
        Default(UnsetValue),
    )
    occupancyTrend: ParkingOccupancyTrendEnumGInput | UnsetValueType = (
        DataclassValidator(ParkingOccupancyTrendEnumGInput),
        Default(UnsetValue),
    )
    parkingNotAllowed: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    probability: PercentageValueInput | UnsetValueType = DataclassValidator(PercentageValueInput), Default(UnsetValue)
    vehicleCountAndRate: list[VehicleCountAndRateInput] | UnsetValueType = (
        ListValidator(DataclassValidator(VehicleCountAndRateInput)),
        Default(UnsetValue),
    )
    overrideThresholdConfiguration: ThresholdConfigurationInput | UnsetValueType = (
        DataclassValidator(ThresholdConfigurationInput),
        Default(UnsetValue),
    )
    prkOccupancyExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
