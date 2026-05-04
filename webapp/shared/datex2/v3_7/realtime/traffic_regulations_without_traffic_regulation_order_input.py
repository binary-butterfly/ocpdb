"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput

from .traffic_regulation_g_input import TrafficRegulationGInput


@validataclass
class TrafficRegulationsWithoutTrafficRegulationOrderInput(ValidataclassMixin):
    trafficRegulation: list[TrafficRegulationGInput] = ListValidator(DataclassValidator(TrafficRegulationGInput))
    troTrafficRegulationsWithoutTrafficRegulationOrderExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
