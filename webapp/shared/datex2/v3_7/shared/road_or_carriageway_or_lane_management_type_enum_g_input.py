"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator

from .road_or_carriageway_or_lane_management_type_enum import RoadOrCarriagewayOrLaneManagementTypeEnum
from .road_or_carriageway_or_lane_management_type_enum_extension_type_g import (
    RoadOrCarriagewayOrLaneManagementTypeEnumExtensionTypeG,
)


@validataclass
class RoadOrCarriagewayOrLaneManagementTypeEnumGInput(ValidataclassMixin):
    value: RoadOrCarriagewayOrLaneManagementTypeEnum = EnumValidator(RoadOrCarriagewayOrLaneManagementTypeEnum)
    extendedValueG: RoadOrCarriagewayOrLaneManagementTypeEnumExtensionTypeG | UnsetValueType = (
        EnumValidator(RoadOrCarriagewayOrLaneManagementTypeEnumExtensionTypeG),
        Default(UnsetValue),
    )
