"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput

from .traffic_regulation_order_g_input import TrafficRegulationOrderGInput


@validataclass
class TrafficRegulationsFromCompetentAuthoritiesInput(ValidataclassMixin):
    trafficRegulationOrder: list[TrafficRegulationOrderGInput] = ListValidator(
        DataclassValidator(TrafficRegulationOrderGInput)
    )
    troTrafficRegulationsFromCompetentAuthoritiesExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
