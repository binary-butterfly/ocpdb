"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator

from .extension_type_g_input import ExtensionTypeGInput
from .multilingual_string_input import MultilingualStringInput


@validataclass
class MandatoryRoadOrCarriagewayOrLaneUsageInput(ValidataclassMixin):
    exclusive: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    respectMandatoryTraffic: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    segregatedLanes: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    contraflowLane: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    otherObligation: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    troTypeOfRegulationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    troMandatoryRoadOrCarriagewayOrLaneUsageExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
