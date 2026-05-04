"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .advisory_speed_input import AdvisorySpeedInput
from .compulsory_min_speed_input import CompulsoryMinSpeedInput
from .max_speed_limit_input import MaxSpeedLimitInput
from .walking_speed_input import WalkingSpeedInput


@validataclass
class SpeedLimitGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    troWalkingSpeed: WalkingSpeedInput | UnsetValueType = DataclassValidator(WalkingSpeedInput), Default(UnsetValue)
    troMaxSpeedLimit: MaxSpeedLimitInput | UnsetValueType = DataclassValidator(MaxSpeedLimitInput), Default(UnsetValue)
    troAdvisorySpeed: AdvisorySpeedInput | UnsetValueType = DataclassValidator(AdvisorySpeedInput), Default(UnsetValue)
    troCompulsoryMinSpeed: CompulsoryMinSpeedInput | UnsetValueType = (
        DataclassValidator(CompulsoryMinSpeedInput),
        Default(UnsetValue),
    )
