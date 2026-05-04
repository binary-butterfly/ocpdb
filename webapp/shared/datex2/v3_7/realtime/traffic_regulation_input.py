"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator, StringValidator

from webapp.shared.datex2.v3_7.shared.activation_status_enum_g_input import ActivationStatusEnumGInput
from webapp.shared.datex2.v3_7.shared.condition_g_input import ConditionGInput
from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput

from .permit_information_input import PermitInformationInput
from .road_sign_g_input import RoadSignGInput
from .type_of_regulation_g_input import TypeOfRegulationGInput


@validataclass
class TrafficRegulationInput(ValidataclassMixin):
    idG: str = StringValidator()
    versionG: str = StringValidator()
    status: ActivationStatusEnumGInput | UnsetValueType = (
        DataclassValidator(ActivationStatusEnumGInput),
        Default(UnsetValue),
    )
    roadSign: list[RoadSignGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(RoadSignGInput)),
        Default(UnsetValue),
    )
    typeOfRegulation: list[TypeOfRegulationGInput] | UnsetValueType = (
        ListValidator(DataclassValidator(TypeOfRegulationGInput)),
        Default(UnsetValue),
    )
    condition: ConditionGInput | UnsetValueType = DataclassValidator(ConditionGInput), Default(UnsetValue)
    permitInformation: list[PermitInformationInput] | UnsetValueType = (
        ListValidator(DataclassValidator(PermitInformationInput)),
        Default(UnsetValue),
    )
    troTrafficRegulationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
