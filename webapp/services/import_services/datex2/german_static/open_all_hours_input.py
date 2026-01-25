"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .closure_information_input import ClosureInformationInput
from .extension_type_g_input import ExtensionTypeGInput


@validataclass
class OpenAllHoursInput:
    closureInformation: ClosureInformationInput | UnsetValueType = (
        DataclassValidator(ClosureInformationInput),
        Default(UnsetValue),
    )
    afacOperatingHoursExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    afacOpenAllHoursExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
