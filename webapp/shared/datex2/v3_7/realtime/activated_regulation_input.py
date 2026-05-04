"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator, StringValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.multilingual_string_input import MultilingualStringInput

from .traffic_regulation_g_input import TrafficRegulationGInput


@validataclass
class ActivatedRegulationInput(ValidataclassMixin):
    actor: MultilingualStringInput = DataclassValidator(MultilingualStringInput)
    issuingAuthority: MultilingualStringInput = DataclassValidator(MultilingualStringInput)
    regulationId: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    trafficRegulation: list[TrafficRegulationGInput] = ListValidator(DataclassValidator(TrafficRegulationGInput))
    troActivatedRegulationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
