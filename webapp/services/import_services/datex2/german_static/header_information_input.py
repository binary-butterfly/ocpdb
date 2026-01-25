"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .confidentiality_value_enum_g_input import ConfidentialityValueEnumGInput
from .extension_type_g_input import ExtensionTypeGInput
from .information_status_enum_g_input import InformationStatusEnumGInput


@validataclass
class HeaderInformationInput:
    confidentiality: ConfidentialityValueEnumGInput | UnsetValueType = (
        DataclassValidator(ConfidentialityValueEnumGInput),
        Default(UnsetValue),
    )
    informationStatus: InformationStatusEnumGInput = DataclassValidator(InformationStatusEnumGInput)
    comHeaderInformationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
