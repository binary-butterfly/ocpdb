"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.road_or_carriageway_or_lane_layout_type_g_input import (
    RoadOrCarriagewayOrLaneLayoutTypeGInput,
)
from webapp.shared.datex2.v3_7.shared.road_or_carriageway_or_lane_status_g_input import (
    RoadOrCarriagewayOrLaneStatusGInput,
)
from webapp.shared.datex2.v3_7.shared.speed_limit_g_input import SpeedLimitGInput

from .network_location_g_input import NetworkLocationGInput


@validataclass
class AlternateRoadOrCarriagewayOrLaneLayoutInput(ValidataclassMixin):
    roadOrCarriagewayOrLaneLayoutType: RoadOrCarriagewayOrLaneLayoutTypeGInput | UnsetValueType = (
        DataclassValidator(RoadOrCarriagewayOrLaneLayoutTypeGInput),
        Default(UnsetValue),
    )
    roadOrCarriagewayOrLaneStatus: RoadOrCarriagewayOrLaneStatusGInput = DataclassValidator(
        RoadOrCarriagewayOrLaneStatusGInput
    )
    temporaryMarkings: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    newLayout: NetworkLocationGInput | UnsetValueType = DataclassValidator(NetworkLocationGInput), Default(UnsetValue)
    speedLimit: SpeedLimitGInput | UnsetValueType = DataclassValidator(SpeedLimitGInput), Default(UnsetValue)
    troTypeOfRegulationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    troAlternateRoadOrCarriagewayOrLaneLayoutExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
