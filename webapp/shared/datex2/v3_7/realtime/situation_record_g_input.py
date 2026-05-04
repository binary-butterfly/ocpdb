"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .abnormal_traffic_input import AbnormalTrafficInput
from .accident_input import AccidentInput
from .animal_presence_obstruction_input import AnimalPresenceObstructionInput
from .authority_operation_input import AuthorityOperationInput
from .conditions_input import ConditionsInput
from .construction_works_input import ConstructionWorksInput
from .disturbance_activity_input import DisturbanceActivityInput
from .environmental_obstruction_input import EnvironmentalObstructionInput
from .equipment_or_system_fault_input import EquipmentOrSystemFaultInput
from .general_instruction_or_message_to_road_users_input import GeneralInstructionOrMessageToRoadUsersInput
from .general_network_management_input import GeneralNetworkManagementInput
from .general_obstruction_input import GeneralObstructionInput
from .generic_situation_record_input import GenericSituationRecordInput
from .infrastructure_damage_obstruction_input import InfrastructureDamageObstructionInput
from .maintenance_works_input import MaintenanceWorksInput
from .non_weather_related_road_conditions_input import NonWeatherRelatedRoadConditionsInput
from .poor_environment_conditions_input import PoorEnvironmentConditionsInput
from .public_event_input import PublicEventInput
from .rerouting_management_input import ReroutingManagementInput
from .road_operator_service_disruption_input import RoadOperatorServiceDisruptionInput
from .road_or_carriageway_or_lane_management_input import RoadOrCarriagewayOrLaneManagementInput
from .roadside_assistance_input import RoadsideAssistanceInput
from .service_disruption_input import ServiceDisruptionInput
from .speed_management_input import SpeedManagementInput
from .transit_information_input import TransitInformationInput
from .vehicle_obstruction_input import VehicleObstructionInput
from .weather_related_road_conditions_input import WeatherRelatedRoadConditionsInput
from .winter_driving_management_input import WinterDrivingManagementInput


@validataclass
class SituationRecordGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    sitInfrastructureDamageObstruction: InfrastructureDamageObstructionInput | UnsetValueType = (
        DataclassValidator(InfrastructureDamageObstructionInput),
        Default(UnsetValue),
    )
    sitEnvironmentalObstruction: EnvironmentalObstructionInput | UnsetValueType = (
        DataclassValidator(EnvironmentalObstructionInput),
        Default(UnsetValue),
    )
    sitAnimalPresenceObstruction: AnimalPresenceObstructionInput | UnsetValueType = (
        DataclassValidator(AnimalPresenceObstructionInput),
        Default(UnsetValue),
    )
    sitGeneralObstruction: GeneralObstructionInput | UnsetValueType = (
        DataclassValidator(GeneralObstructionInput),
        Default(UnsetValue),
    )
    sitVehicleObstruction: VehicleObstructionInput | UnsetValueType = (
        DataclassValidator(VehicleObstructionInput),
        Default(UnsetValue),
    )
    sitDisturbanceActivity: DisturbanceActivityInput | UnsetValueType = (
        DataclassValidator(DisturbanceActivityInput),
        Default(UnsetValue),
    )
    sitPublicEvent: PublicEventInput | UnsetValueType = DataclassValidator(PublicEventInput), Default(UnsetValue)
    sitAuthorityOperation: AuthorityOperationInput | UnsetValueType = (
        DataclassValidator(AuthorityOperationInput),
        Default(UnsetValue),
    )
    sitAbnormalTraffic: AbnormalTrafficInput | UnsetValueType = (
        DataclassValidator(AbnormalTrafficInput),
        Default(UnsetValue),
    )
    sitEquipmentOrSystemFault: EquipmentOrSystemFaultInput | UnsetValueType = (
        DataclassValidator(EquipmentOrSystemFaultInput),
        Default(UnsetValue),
    )
    sitAccident: AccidentInput | UnsetValueType = DataclassValidator(AccidentInput), Default(UnsetValue)
    sitConditions: ConditionsInput | UnsetValueType = DataclassValidator(ConditionsInput), Default(UnsetValue)
    sitNonWeatherRelatedRoadConditions: NonWeatherRelatedRoadConditionsInput | UnsetValueType = (
        DataclassValidator(NonWeatherRelatedRoadConditionsInput),
        Default(UnsetValue),
    )
    sitWeatherRelatedRoadConditions: WeatherRelatedRoadConditionsInput | UnsetValueType = (
        DataclassValidator(WeatherRelatedRoadConditionsInput),
        Default(UnsetValue),
    )
    sitPoorEnvironmentConditions: PoorEnvironmentConditionsInput | UnsetValueType = (
        DataclassValidator(PoorEnvironmentConditionsInput),
        Default(UnsetValue),
    )
    sitGenericSituationRecord: GenericSituationRecordInput | UnsetValueType = (
        DataclassValidator(GenericSituationRecordInput),
        Default(UnsetValue),
    )
    sitRoadOperatorServiceDisruption: RoadOperatorServiceDisruptionInput | UnsetValueType = (
        DataclassValidator(RoadOperatorServiceDisruptionInput),
        Default(UnsetValue),
    )
    sitServiceDisruption: ServiceDisruptionInput | UnsetValueType = (
        DataclassValidator(ServiceDisruptionInput),
        Default(UnsetValue),
    )
    sitTransitInformation: TransitInformationInput | UnsetValueType = (
        DataclassValidator(TransitInformationInput),
        Default(UnsetValue),
    )
    sitReroutingManagement: ReroutingManagementInput | UnsetValueType = (
        DataclassValidator(ReroutingManagementInput),
        Default(UnsetValue),
    )
    sitRoadOrCarriagewayOrLaneManagement: RoadOrCarriagewayOrLaneManagementInput | UnsetValueType = (
        DataclassValidator(RoadOrCarriagewayOrLaneManagementInput),
        Default(UnsetValue),
    )
    sitSpeedManagement: SpeedManagementInput | UnsetValueType = (
        DataclassValidator(SpeedManagementInput),
        Default(UnsetValue),
    )
    sitGeneralInstructionOrMessageToRoadUsers: GeneralInstructionOrMessageToRoadUsersInput | UnsetValueType = (
        DataclassValidator(GeneralInstructionOrMessageToRoadUsersInput),
        Default(UnsetValue),
    )
    sitWinterDrivingManagement: WinterDrivingManagementInput | UnsetValueType = (
        DataclassValidator(WinterDrivingManagementInput),
        Default(UnsetValue),
    )
    sitGeneralNetworkManagement: GeneralNetworkManagementInput | UnsetValueType = (
        DataclassValidator(GeneralNetworkManagementInput),
        Default(UnsetValue),
    )
    sitConstructionWorks: ConstructionWorksInput | UnsetValueType = (
        DataclassValidator(ConstructionWorksInput),
        Default(UnsetValue),
    )
    sitMaintenanceWorks: MaintenanceWorksInput | UnsetValueType = (
        DataclassValidator(MaintenanceWorksInput),
        Default(UnsetValue),
    )
    sitRoadsideAssistance: RoadsideAssistanceInput | UnsetValueType = (
        DataclassValidator(RoadsideAssistanceInput),
        Default(UnsetValue),
    )
