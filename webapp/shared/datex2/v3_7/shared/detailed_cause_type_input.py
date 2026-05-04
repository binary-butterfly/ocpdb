"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator

from .abnormal_traffic_type_enum_g_input import AbnormalTrafficTypeEnumGInput
from .accident_type_enum_g_input import AccidentTypeEnumGInput
from .animal_presence_type_enum_g_input import AnimalPresenceTypeEnumGInput
from .authority_operation_type_enum_g_input import AuthorityOperationTypeEnumGInput
from .construction_work_type_enum_g_input import ConstructionWorkTypeEnumGInput
from .disturbance_activity_type_enum_g_input import DisturbanceActivityTypeEnumGInput
from .driving_condition_type_enum_g_input import DrivingConditionTypeEnumGInput
from .environmental_obstruction_type_enum_g_input import EnvironmentalObstructionTypeEnumGInput
from .equipment_or_system_fault_type_enum_g_input import EquipmentOrSystemFaultTypeEnumGInput
from .extension_type_g_input import ExtensionTypeGInput
from .general_instruction_to_road_users_type_enum_g_input import GeneralInstructionToRoadUsersTypeEnumGInput
from .general_network_management_type_enum_g_input import GeneralNetworkManagementTypeEnumGInput
from .infrastructure_damage_type_enum_g_input import InfrastructureDamageTypeEnumGInput
from .non_weather_related_road_condition_type_enum_g_input import NonWeatherRelatedRoadConditionTypeEnumGInput
from .obstruction_type_enum_g_input import ObstructionTypeEnumGInput
from .poor_environment_type_enum_g_input import PoorEnvironmentTypeEnumGInput
from .public_event_type_enum_g_input import PublicEventTypeEnumGInput
from .rerouting_management_type_enum_g_input import ReroutingManagementTypeEnumGInput
from .road_maintenance_type_enum_g_input import RoadMaintenanceTypeEnumGInput
from .road_operator_service_disruption_type_enum_g_input import RoadOperatorServiceDisruptionTypeEnumGInput
from .road_or_carriageway_or_lane_management_type_enum_g_input import RoadOrCarriagewayOrLaneManagementTypeEnumGInput
from .roadside_assistance_type_enum_g_input import RoadsideAssistanceTypeEnumGInput
from .service_disruption_type_enum_g_input import ServiceDisruptionTypeEnumGInput
from .speed_management_type_enum_g_input import SpeedManagementTypeEnumGInput
from .transit_service_information_enum_g_input import TransitServiceInformationEnumGInput
from .vehicle_obstruction_type_enum_g_input import VehicleObstructionTypeEnumGInput
from .weather_related_road_condition_type_enum_g_input import WeatherRelatedRoadConditionTypeEnumGInput
from .winter_equipment_management_type_enum_g_input import WinterEquipmentManagementTypeEnumGInput


@validataclass
class DetailedCauseTypeInput(ValidataclassMixin):
    abnormalTrafficType: AbnormalTrafficTypeEnumGInput | UnsetValueType = (
        DataclassValidator(AbnormalTrafficTypeEnumGInput),
        Default(UnsetValue),
    )
    accidentType: list[AccidentTypeEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(AccidentTypeEnumGInput)),
        Default(UnsetValue),
    )
    animalPresenceType: AnimalPresenceTypeEnumGInput | UnsetValueType = (
        DataclassValidator(AnimalPresenceTypeEnumGInput),
        Default(UnsetValue),
    )
    authorityOperationType: AuthorityOperationTypeEnumGInput | UnsetValueType = (
        DataclassValidator(AuthorityOperationTypeEnumGInput),
        Default(UnsetValue),
    )
    constructionWorkType: ConstructionWorkTypeEnumGInput | UnsetValueType = (
        DataclassValidator(ConstructionWorkTypeEnumGInput),
        Default(UnsetValue),
    )
    disturbanceActivityType: DisturbanceActivityTypeEnumGInput | UnsetValueType = (
        DataclassValidator(DisturbanceActivityTypeEnumGInput),
        Default(UnsetValue),
    )
    drivingConditionType: DrivingConditionTypeEnumGInput | UnsetValueType = (
        DataclassValidator(DrivingConditionTypeEnumGInput),
        Default(UnsetValue),
    )
    environmentalObstructionType: EnvironmentalObstructionTypeEnumGInput | UnsetValueType = (
        DataclassValidator(EnvironmentalObstructionTypeEnumGInput),
        Default(UnsetValue),
    )
    equipmentOrSystemFaultType: EquipmentOrSystemFaultTypeEnumGInput | UnsetValueType = (
        DataclassValidator(EquipmentOrSystemFaultTypeEnumGInput),
        Default(UnsetValue),
    )
    generalInstructionToRoadUsersType: GeneralInstructionToRoadUsersTypeEnumGInput | UnsetValueType = (
        DataclassValidator(GeneralInstructionToRoadUsersTypeEnumGInput),
        Default(UnsetValue),
    )
    generalNetworkManagementType: GeneralNetworkManagementTypeEnumGInput | UnsetValueType = (
        DataclassValidator(GeneralNetworkManagementTypeEnumGInput),
        Default(UnsetValue),
    )
    infrastructureDamageType: InfrastructureDamageTypeEnumGInput | UnsetValueType = (
        DataclassValidator(InfrastructureDamageTypeEnumGInput),
        Default(UnsetValue),
    )
    nonWeatherRelatedRoadConditionType: list[NonWeatherRelatedRoadConditionTypeEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(NonWeatherRelatedRoadConditionTypeEnumGInput)),
        Default(UnsetValue),
    )
    obstructionType: list[ObstructionTypeEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(ObstructionTypeEnumGInput)),
        Default(UnsetValue),
    )
    poorEnvironmentType: list[PoorEnvironmentTypeEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(PoorEnvironmentTypeEnumGInput)),
        Default(UnsetValue),
    )
    publicEventType: PublicEventTypeEnumGInput | UnsetValueType = (
        DataclassValidator(PublicEventTypeEnumGInput),
        Default(UnsetValue),
    )
    reroutingManagementType: list[ReroutingManagementTypeEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(ReroutingManagementTypeEnumGInput)),
        Default(UnsetValue),
    )
    roadMaintenanceType: list[RoadMaintenanceTypeEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(RoadMaintenanceTypeEnumGInput)),
        Default(UnsetValue),
    )
    roadOperatorServiceDisruptionType: list[RoadOperatorServiceDisruptionTypeEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(RoadOperatorServiceDisruptionTypeEnumGInput)),
        Default(UnsetValue),
    )
    roadOrCarriagewayOrLaneManagementType: RoadOrCarriagewayOrLaneManagementTypeEnumGInput | UnsetValueType = (
        DataclassValidator(RoadOrCarriagewayOrLaneManagementTypeEnumGInput),
        Default(UnsetValue),
    )
    roadsideAssistanceType: RoadsideAssistanceTypeEnumGInput | UnsetValueType = (
        DataclassValidator(RoadsideAssistanceTypeEnumGInput),
        Default(UnsetValue),
    )
    roadsideServiceDisruptionType: list[ServiceDisruptionTypeEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(ServiceDisruptionTypeEnumGInput)),
        Default(UnsetValue),
    )
    speedManagementType: SpeedManagementTypeEnumGInput | UnsetValueType = (
        DataclassValidator(SpeedManagementTypeEnumGInput),
        Default(UnsetValue),
    )
    transitServiceInformation: TransitServiceInformationEnumGInput | UnsetValueType = (
        DataclassValidator(TransitServiceInformationEnumGInput),
        Default(UnsetValue),
    )
    vehicleObstructionType: VehicleObstructionTypeEnumGInput | UnsetValueType = (
        DataclassValidator(VehicleObstructionTypeEnumGInput),
        Default(UnsetValue),
    )
    weatherRelatedRoadConditionType: list[WeatherRelatedRoadConditionTypeEnumGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(WeatherRelatedRoadConditionTypeEnumGInput)),
        Default(UnsetValue),
    )
    winterEquipmentManagementType: WinterEquipmentManagementTypeEnumGInput | UnsetValueType = (
        DataclassValidator(WinterEquipmentManagementTypeEnumGInput),
        Default(UnsetValue),
    )
    sitDetailedCauseTypeExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
