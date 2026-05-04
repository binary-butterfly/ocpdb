"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, IntegerValidator

from .extension_type_g_input import ExtensionTypeGInput
from .lane_enum_g_input import LaneEnumGInput


@validataclass
class LaneInput(ValidataclassMixin):
    laneNumber: int | UnsetValueType = IntegerValidator(), Default(UnsetValue)
    laneUsage: LaneEnumGInput | UnsetValueType = DataclassValidator(LaneEnumGInput), Default(UnsetValue)
    locLaneExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
