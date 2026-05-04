"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator

from .lane_enum import LaneEnum
from .lane_enum_extension_type_g import LaneEnumExtensionTypeG


@validataclass
class LaneEnumGInput(ValidataclassMixin):
    value: LaneEnum = EnumValidator(LaneEnum)
    extendedValueG: LaneEnumExtensionTypeG | UnsetValueType = EnumValidator(LaneEnumExtensionTypeG), Default(UnsetValue)
