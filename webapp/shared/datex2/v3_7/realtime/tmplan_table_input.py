"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from datetime import datetime

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, DateTimeValidator, ListValidator, StringValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput

from .action_g_input import ActionGInput
from .measure_g_input import MeasureGInput
from .scenario_input import ScenarioInput


@validataclass
class TmplanTableInput(ValidataclassMixin):
    idG: str = StringValidator()
    versionG: str = StringValidator()
    externalIdentification: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    versionTime: datetime = DateTimeValidator()
    description: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    scenario: list[ScenarioInput] | UnsetValueType = (
        ListValidator(DataclassValidator(ScenarioInput)),
        Default(UnsetValue),
    )
    measure: list[MeasureGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(MeasureGInput)),
        Default(UnsetValue),
    )
    action: list[ActionGInput] | UnsetValueType = ListValidator(DataclassValidator(ActionGInput)), Default(UnsetValue)
    tmpTmplanTableExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
