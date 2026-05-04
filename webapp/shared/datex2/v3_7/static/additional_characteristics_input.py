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
    StringValidator,
)

from webapp.shared.datex2.v3_7.shared.dedicated_access_input import DedicatedAccessInput
from webapp.shared.datex2.v3_7.shared.dimension_input import DimensionInput
from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.parking_mode_enum_g_input import ParkingModeEnumGInput
from webapp.shared.datex2.v3_7.shared.parking_space_convenience_enum_g_input import ParkingSpaceConvenienceEnumGInput
from webapp.shared.datex2.v3_7.shared.parking_space_occupancy_detection_enum_g_input import (
    ParkingSpaceOccupancyDetectionEnumGInput,
)
from webapp.shared.datex2.v3_7.shared.parking_structural_characteristics_enum_g_input import (
    ParkingStructuralCharacteristicsEnumGInput,
)

from .assignment_input import AssignmentInput


@validataclass
class AdditionalCharacteristicsInput(ValidataclassMixin):
    floor: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    weightLimit: float | UnsetValueType = FloatValidator(allow_integers=True), Default(UnsetValue)
    additionalConvenience: list[ParkingSpaceConvenienceEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(ParkingSpaceConvenienceEnumGInput)),
        Default(UnsetValue),
    )
    structuralCharacteristics: list[ParkingStructuralCharacteristicsEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(ParkingStructuralCharacteristicsEnumGInput)),
        Default(UnsetValue),
    )
    parkingMode: ParkingModeEnumGInput | UnsetValueType = DataclassValidator(ParkingModeEnumGInput), Default(UnsetValue)
    occupancyDetection: ParkingSpaceOccupancyDetectionEnumGInput | UnsetValueType = (
        DataclassValidator(ParkingSpaceOccupancyDetectionEnumGInput),
        Default(UnsetValue),
    )
    temporarilyParking: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    distanceFromPrimaryRoad: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    assignment: list[AssignmentInput] | UnsetValueType = (
        ListValidator(DataclassValidator(AssignmentInput)),
        Default(UnsetValue),
    )
    dedicatedAccess: list[DedicatedAccessInput] | UnsetValueType = (
        ListValidator(DataclassValidator(DedicatedAccessInput)),
        Default(UnsetValue),
    )
    totalDimension: DimensionInput | UnsetValueType = DataclassValidator(DimensionInput), Default(UnsetValue)
    minimumParkingSpaceDimension: DimensionInput | UnsetValueType = (
        DataclassValidator(DimensionInput),
        Default(UnsetValue),
    )
    maximumParkingSpaceDimension: DimensionInput | UnsetValueType = (
        DataclassValidator(DimensionInput),
        Default(UnsetValue),
    )
    prkAdditionalCharacteristicsExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
