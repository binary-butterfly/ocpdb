"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput

from .dynamic_traffic_regulation_g_input import DynamicTrafficRegulationGInput


@validataclass
class DynamicTrafficRegulationsInput(ValidataclassMixin):
    dynamicTrafficRegulation: list[DynamicTrafficRegulationGInput] = ListValidator(
        DataclassValidator(DynamicTrafficRegulationGInput)
    )
    troDynamicTrafficRegulationsExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
