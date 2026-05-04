"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, IntegerValidator, ListValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput
from webapp.shared.datex2.v3_7.shared.overall_period_input import OverallPeriodInput
from webapp.shared.datex2.v3_7.shared.parking_usage_scenario_enum_g_input import ParkingUsageScenarioEnumGInput
from webapp.shared.datex2.v3_7.shared.public_event_type_enum_g_input import PublicEventTypeEnumGInput
from webapp.shared.datex2.v3_7.shared.truck_parking_dynamic_management_enum_g_input import (
    TruckParkingDynamicManagementEnumGInput,
)

from .related_location_g_input import RelatedLocationGInput


@validataclass
class UsageScenarioInput(ValidataclassMixin):
    operatingPatternIndex: int = IntegerValidator()
    type: list[ParkingUsageScenarioEnumGInput] = ListValidator(DataclassValidator(ParkingUsageScenarioEnumGInput))
    description: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    truckParkingDynamicManagement: list[TruckParkingDynamicManagementEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(TruckParkingDynamicManagementEnumGInput)),
        Default(UnsetValue),
    )
    eventParkingType: PublicEventTypeEnumGInput | UnsetValueType = (
        DataclassValidator(PublicEventTypeEnumGInput),
        Default(UnsetValue),
    )
    relatedLocation: list[RelatedLocationGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(RelatedLocationGInput)),
        Default(UnsetValue),
    )
    validity: OverallPeriodInput | UnsetValueType = DataclassValidator(OverallPeriodInput), Default(UnsetValue)
    prkOperatingPatternExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    prkUsageScenarioExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
