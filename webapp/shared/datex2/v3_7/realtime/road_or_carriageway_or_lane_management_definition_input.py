"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator, IntegerValidator, ListValidator

from webapp.shared.datex2.v3_7.shared.compliance_option_enum_g_input import ComplianceOptionEnumGInput
from webapp.shared.datex2.v3_7.shared.direction_enum_g_input import DirectionEnumGInput
from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.places_enum_g_input import PlacesEnumGInput
from webapp.shared.datex2.v3_7.shared.road_or_carriageway_or_lane_management_type_enum_g_input import (
    RoadOrCarriagewayOrLaneManagementTypeEnumGInput,
)
from webapp.shared.datex2.v3_7.shared.traffic_type_enum_g_input import TrafficTypeEnumGInput

from .location_reference_g_input import LocationReferenceGInput
from .vehicle_characteristics_input import VehicleCharacteristicsInput


@validataclass
class RoadOrCarriagewayOrLaneManagementDefinitionInput(ValidataclassMixin):
    complianceOption: ComplianceOptionEnumGInput = DataclassValidator(ComplianceOptionEnumGInput)
    applicableForTrafficDirection: list[DirectionEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(DirectionEnumGInput)),
        Default(UnsetValue),
    )
    applicableForTrafficType: list[TrafficTypeEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(TrafficTypeEnumGInput)),
        Default(UnsetValue),
    )
    placesAtWhichApplicable: list[PlacesEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(PlacesEnumGInput)),
        Default(UnsetValue),
    )
    automaticallyInitiated: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    roadOrCarriagewayOrLaneManagementType: RoadOrCarriagewayOrLaneManagementTypeEnumGInput = DataclassValidator(
        RoadOrCarriagewayOrLaneManagementTypeEnumGInput
    )
    minimumCarOccupancy: int | UnsetValueType = IntegerValidator(min_value=0), Default(UnsetValue)
    targetLocation: list[LocationReferenceGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(LocationReferenceGInput)),
        Default(UnsetValue),
    )
    forVehiclesWithCharacteristicsOf: list[VehicleCharacteristicsInput] | UnsetValueType = (
        ListValidator(DataclassValidator(VehicleCharacteristicsInput)),
        Default(UnsetValue),
    )
    tmpOperatorActionDefinitionExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    tmpNetworkManagementDefinitionExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    tmpRoadOrCarriagewayOrLaneManagementDefinitionExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
