"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .ambient_warning_input import AmbientWarningInput
from .road_warning_input import RoadWarningInput
from .steep_hill_input import SteepHillInput
from .traffic_ahead_input import TrafficAheadInput


@validataclass
class WarningGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    troRoadWarning: RoadWarningInput | UnsetValueType = DataclassValidator(RoadWarningInput), Default(UnsetValue)
    troSteepHill: SteepHillInput | UnsetValueType = DataclassValidator(SteepHillInput), Default(UnsetValue)
    troAmbientWarning: AmbientWarningInput | UnsetValueType = (
        DataclassValidator(AmbientWarningInput),
        Default(UnsetValue),
    )
    troTrafficAhead: TrafficAheadInput | UnsetValueType = DataclassValidator(TrafficAheadInput), Default(UnsetValue)
