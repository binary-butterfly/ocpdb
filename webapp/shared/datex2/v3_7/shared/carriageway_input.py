"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, IntegerValidator, ListValidator

from .carriageway_enum_g_input import CarriagewayEnumGInput
from .extension_type_g_input import ExtensionTypeGInput
from .lane_input import LaneInput


@validataclass
class CarriagewayInput(ValidataclassMixin):
    carriageway: CarriagewayEnumGInput = DataclassValidator(CarriagewayEnumGInput)
    originalNumberOfLanes: int | UnsetValueType = IntegerValidator(), Default(UnsetValue)
    lane: list[LaneInput] | UnsetValueType = ListValidator(DataclassValidator(LaneInput)), Default(UnsetValue)
    locCarriagewayExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
