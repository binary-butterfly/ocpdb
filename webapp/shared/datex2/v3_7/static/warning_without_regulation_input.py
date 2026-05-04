"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator

from webapp.shared.datex2.v3_7.shared.condition_g_input import ConditionGInput
from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.warning_g_input import WarningGInput

from .road_sign_g_input import RoadSignGInput


@validataclass
class WarningWithoutRegulationInput(ValidataclassMixin):
    typeOfWarningWithoutRegulation: list[WarningGInput] = ListValidator(DataclassValidator(WarningGInput))
    condition: ConditionGInput | UnsetValueType = DataclassValidator(ConditionGInput), Default(UnsetValue)
    roadSign: list[RoadSignGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(RoadSignGInput)),
        Default(UnsetValue),
    )
    troWarningWithoutRegulationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
