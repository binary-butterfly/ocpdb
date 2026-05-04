"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator, ListValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.priority_rule_type_enum_g_input import PriorityRuleTypeEnumGInput

from .vehicle_characteristics_input import VehicleCharacteristicsInput


@validataclass
class PriorityRuleInput(ValidataclassMixin):
    priorityRuleType: list[PriorityRuleTypeEnumGInput] = ListValidator(DataclassValidator(PriorityRuleTypeEnumGInput))
    respectBicycle: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    giveWayTo: list[VehicleCharacteristicsInput] | UnsetValueType = (
        ListValidator(DataclassValidator(VehicleCharacteristicsInput)),
        Default(UnsetValue),
    )
    troTypeOfRegulationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    troPriorityRuleExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
