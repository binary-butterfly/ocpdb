"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.traffic_regulation_installer_type_enum_g_input import (
    TrafficRegulationInstallerTypeEnumGInput,
)

from .traffic_regulation_g_input import TrafficRegulationGInput


@validataclass
class AdHocTrafficRegulationInput(ValidataclassMixin):
    installer: TrafficRegulationInstallerTypeEnumGInput = DataclassValidator(TrafficRegulationInstallerTypeEnumGInput)
    trafficRegulation: list[TrafficRegulationGInput] = ListValidator(DataclassValidator(TrafficRegulationGInput))
    troAdHocTrafficRegulationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
