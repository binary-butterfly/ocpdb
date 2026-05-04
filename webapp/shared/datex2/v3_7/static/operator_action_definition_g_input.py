"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .general_instruction_or_message_to_road_users_definition_input import (
    GeneralInstructionOrMessageToRoadUsersDefinitionInput,
)
from .general_network_management_definition_input import GeneralNetworkManagementDefinitionInput
from .rerouting_management_definition_input import ReroutingManagementDefinitionInput
from .road_or_carriageway_or_lane_management_definition_input import RoadOrCarriagewayOrLaneManagementDefinitionInput
from .roadside_assistance_definition_input import RoadsideAssistanceDefinitionInput
from .sign_setting_definition_input import SignSettingDefinitionInput
from .speed_management_definition_input import SpeedManagementDefinitionInput
from .traffic_signal_setting_definition_input import TrafficSignalSettingDefinitionInput
from .winter_driving_management_definition_input import WinterDrivingManagementDefinitionInput


@validataclass
class OperatorActionDefinitionGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    tmpSignSettingDefinition: SignSettingDefinitionInput | UnsetValueType = (
        DataclassValidator(SignSettingDefinitionInput),
        Default(UnsetValue),
    )
    tmpGeneralInstructionOrMessageToRoadUsersDefinition: (
        GeneralInstructionOrMessageToRoadUsersDefinitionInput | UnsetValueType
    ) = DataclassValidator(GeneralInstructionOrMessageToRoadUsersDefinitionInput), Default(UnsetValue)
    tmpTrafficSignalSettingDefinition: TrafficSignalSettingDefinitionInput | UnsetValueType = (
        DataclassValidator(TrafficSignalSettingDefinitionInput),
        Default(UnsetValue),
    )
    tmpGeneralNetworkManagementDefinition: GeneralNetworkManagementDefinitionInput | UnsetValueType = (
        DataclassValidator(GeneralNetworkManagementDefinitionInput),
        Default(UnsetValue),
    )
    tmpRoadOrCarriagewayOrLaneManagementDefinition: (
        RoadOrCarriagewayOrLaneManagementDefinitionInput | UnsetValueType
    ) = DataclassValidator(RoadOrCarriagewayOrLaneManagementDefinitionInput), Default(UnsetValue)
    tmpWinterDrivingManagementDefinition: WinterDrivingManagementDefinitionInput | UnsetValueType = (
        DataclassValidator(WinterDrivingManagementDefinitionInput),
        Default(UnsetValue),
    )
    tmpSpeedManagementDefinition: SpeedManagementDefinitionInput | UnsetValueType = (
        DataclassValidator(SpeedManagementDefinitionInput),
        Default(UnsetValue),
    )
    tmpReroutingManagementDefinition: ReroutingManagementDefinitionInput | UnsetValueType = (
        DataclassValidator(ReroutingManagementDefinitionInput),
        Default(UnsetValue),
    )
    tmpRoadsideAssistanceDefinition: RoadsideAssistanceDefinitionInput | UnsetValueType = (
        DataclassValidator(RoadsideAssistanceDefinitionInput),
        Default(UnsetValue),
    )
