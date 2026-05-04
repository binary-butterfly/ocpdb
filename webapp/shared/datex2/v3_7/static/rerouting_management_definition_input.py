"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator, ListValidator

from webapp.shared.datex2.v3_7.shared.compliance_option_enum_g_input import ComplianceOptionEnumGInput
from webapp.shared.datex2.v3_7.shared.direction_enum_g_input import DirectionEnumGInput
from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput
from webapp.shared.datex2.v3_7.shared.places_enum_g_input import PlacesEnumGInput
from webapp.shared.datex2.v3_7.shared.rerouting_type_enum_g_input import ReroutingTypeEnumGInput
from webapp.shared.datex2.v3_7.shared.traffic_type_enum_g_input import TrafficTypeEnumGInput

from .location_g_input import LocationGInput
from .location_reference_g_input import LocationReferenceGInput
from .route_description_input import RouteDescriptionInput
from .vehicle_characteristics_input import VehicleCharacteristicsInput


@validataclass
class ReroutingManagementDefinitionInput(ValidataclassMixin):
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
    name: MultilingualStringInput | UnsetValueType = DataclassValidator(MultilingualStringInput), Default(UnsetValue)
    type: ReroutingTypeEnumGInput | UnsetValueType = DataclassValidator(ReroutingTypeEnumGInput), Default(UnsetValue)
    bindingTrafficRegulation: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    preventiveMeasure: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    targetLocation: list[LocationReferenceGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(LocationReferenceGInput)),
        Default(UnsetValue),
    )
    forVehiclesWithCharacteristicsOf: list[VehicleCharacteristicsInput] | UnsetValueType = (
        ListValidator(DataclassValidator(VehicleCharacteristicsInput)),
        Default(UnsetValue),
    )
    routingOrigin: list[LocationGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(LocationGInput)),
        Default(UnsetValue),
    )
    routingThrough: list[LocationGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(LocationGInput)),
        Default(UnsetValue),
    )
    routingDestination: list[LocationGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(LocationGInput)),
        Default(UnsetValue),
    )
    originalRoute: RouteDescriptionInput | UnsetValueType = (
        DataclassValidator(RouteDescriptionInput),
        Default(UnsetValue),
    )
    alternativeRoute: list[RouteDescriptionInput] | UnsetValueType = (
        ListValidator(DataclassValidator(RouteDescriptionInput)),
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
    tmpReroutingManagementDefinitionExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
