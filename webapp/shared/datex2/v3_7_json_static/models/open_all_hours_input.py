"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .closure_information_input import ClosureInformationInput
from .extension_type_g_input import ExtensionTypeGInput


@validataclass
class OpenAllHoursInput(ValidataclassMixin):
    """
    Open or available all the time (24/7)
    """

    closureInformation: ClosureInformationInput | UnsetValueType = (
        DataclassValidator(ClosureInformationInput),
        Default(UnsetValue),
    )
    facOperatingHoursExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    facOpenAllHoursExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
