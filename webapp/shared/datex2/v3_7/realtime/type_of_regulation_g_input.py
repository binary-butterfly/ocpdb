"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from webapp.shared.datex2.v3_7.shared.access_restriction_input import AccessRestrictionInput
from webapp.shared.datex2.v3_7.shared.advisory_speed_input import AdvisorySpeedInput
from webapp.shared.datex2.v3_7.shared.ambient_warning_input import AmbientWarningInput
from webapp.shared.datex2.v3_7.shared.compulsory_min_speed_input import CompulsoryMinSpeedInput
from webapp.shared.datex2.v3_7.shared.direction_restriction_input import DirectionRestrictionInput
from webapp.shared.datex2.v3_7.shared.hard_shoulder_running_restriction_input import HardShoulderRunningRestrictionInput
from webapp.shared.datex2.v3_7.shared.mandatory_road_or_carriageway_or_lane_usage_input import (
    MandatoryRoadOrCarriagewayOrLaneUsageInput,
)
from webapp.shared.datex2.v3_7.shared.max_speed_limit_input import MaxSpeedLimitInput
from webapp.shared.datex2.v3_7.shared.minimum_distance_restriction_input import MinimumDistanceRestrictionInput
from webapp.shared.datex2.v3_7.shared.rerouting_input import ReroutingInput
from webapp.shared.datex2.v3_7.shared.road_warning_input import RoadWarningInput
from webapp.shared.datex2.v3_7.shared.rush_hour_lane_restriction_input import RushHourLaneRestrictionInput
from webapp.shared.datex2.v3_7.shared.standing_or_parking_control_input import StandingOrParkingControlInput
from webapp.shared.datex2.v3_7.shared.steep_hill_input import SteepHillInput
from webapp.shared.datex2.v3_7.shared.traffic_ahead_input import TrafficAheadInput
from webapp.shared.datex2.v3_7.shared.walking_speed_input import WalkingSpeedInput

from .alternate_road_or_carriageway_or_lane_layout_input import AlternateRoadOrCarriagewayOrLaneLayoutInput
from .priority_rule_input import PriorityRuleInput
from .prohibition_of_overtaking_input import ProhibitionOfOvertakingInput


@validataclass
class TypeOfRegulationGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    troProhibitionOfOvertaking: ProhibitionOfOvertakingInput | UnsetValueType = (
        DataclassValidator(ProhibitionOfOvertakingInput),
        Default(UnsetValue),
    )
    troAlternateRoadOrCarriagewayOrLaneLayout: AlternateRoadOrCarriagewayOrLaneLayoutInput | UnsetValueType = (
        DataclassValidator(AlternateRoadOrCarriagewayOrLaneLayoutInput),
        Default(UnsetValue),
    )
    troMinimumDistanceRestriction: MinimumDistanceRestrictionInput | UnsetValueType = (
        DataclassValidator(MinimumDistanceRestrictionInput),
        Default(UnsetValue),
    )
    troAccessRestriction: AccessRestrictionInput | UnsetValueType = (
        DataclassValidator(AccessRestrictionInput),
        Default(UnsetValue),
    )
    troStandingOrParkingControl: StandingOrParkingControlInput | UnsetValueType = (
        DataclassValidator(StandingOrParkingControlInput),
        Default(UnsetValue),
    )
    troDirectionRestriction: DirectionRestrictionInput | UnsetValueType = (
        DataclassValidator(DirectionRestrictionInput),
        Default(UnsetValue),
    )
    troWalkingSpeed: WalkingSpeedInput | UnsetValueType = DataclassValidator(WalkingSpeedInput), Default(UnsetValue)
    troMaxSpeedLimit: MaxSpeedLimitInput | UnsetValueType = DataclassValidator(MaxSpeedLimitInput), Default(UnsetValue)
    troAdvisorySpeed: AdvisorySpeedInput | UnsetValueType = DataclassValidator(AdvisorySpeedInput), Default(UnsetValue)
    troCompulsoryMinSpeed: CompulsoryMinSpeedInput | UnsetValueType = (
        DataclassValidator(CompulsoryMinSpeedInput),
        Default(UnsetValue),
    )
    troMandatoryRoadOrCarriagewayOrLaneUsage: MandatoryRoadOrCarriagewayOrLaneUsageInput | UnsetValueType = (
        DataclassValidator(MandatoryRoadOrCarriagewayOrLaneUsageInput),
        Default(UnsetValue),
    )
    troRerouting: ReroutingInput | UnsetValueType = DataclassValidator(ReroutingInput), Default(UnsetValue)
    troRoadWarning: RoadWarningInput | UnsetValueType = DataclassValidator(RoadWarningInput), Default(UnsetValue)
    troSteepHill: SteepHillInput | UnsetValueType = DataclassValidator(SteepHillInput), Default(UnsetValue)
    troAmbientWarning: AmbientWarningInput | UnsetValueType = (
        DataclassValidator(AmbientWarningInput),
        Default(UnsetValue),
    )
    troTrafficAhead: TrafficAheadInput | UnsetValueType = DataclassValidator(TrafficAheadInput), Default(UnsetValue)
    troPriorityRule: PriorityRuleInput | UnsetValueType = DataclassValidator(PriorityRuleInput), Default(UnsetValue)
    troHardShoulderRunningRestriction: HardShoulderRunningRestrictionInput | UnsetValueType = (
        DataclassValidator(HardShoulderRunningRestrictionInput),
        Default(UnsetValue),
    )
    troRushHourLaneRestriction: RushHourLaneRestrictionInput | UnsetValueType = (
        DataclassValidator(RushHourLaneRestrictionInput),
        Default(UnsetValue),
    )
