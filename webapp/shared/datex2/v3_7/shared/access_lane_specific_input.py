"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, IntegerValidator

from .access_lane_type_enum_g_input import AccessLaneTypeEnumGInput
from .dimension_input import DimensionInput
from .extension_type_g_input import ExtensionTypeGInput
from .operating_hours_g_input import OperatingHoursGInput


@validataclass
class AccessLaneSpecificInput(ValidataclassMixin):
    sequenceNumber: int = IntegerValidator(min_value=0)
    laneType: AccessLaneTypeEnumGInput = DataclassValidator(AccessLaneTypeEnumGInput)
    maxDimension: DimensionInput | UnsetValueType = DataclassValidator(DimensionInput), Default(UnsetValue)
    entranceOpenTime: OperatingHoursGInput | UnsetValueType = (
        DataclassValidator(OperatingHoursGInput),
        Default(UnsetValue),
    )
    exitOpenTime: OperatingHoursGInput | UnsetValueType = DataclassValidator(OperatingHoursGInput), Default(UnsetValue)
    prkAccessLaneSpecificExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
