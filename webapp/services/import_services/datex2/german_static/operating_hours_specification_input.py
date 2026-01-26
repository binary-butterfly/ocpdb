"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator, StringValidator

from .closure_information_input import ClosureInformationInput
from .extension_type_g_input import ExtensionTypeGInput
from .overall_period_input import OverallPeriodInput


@validataclass
class OperatingHoursSpecificationInput:
    idG: str = StringValidator()
    versionG: str = StringValidator()
    lastUpdated: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    label: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    operatingAllYear: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    urlLinkAddress: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    closureInformation: ClosureInformationInput | UnsetValueType = (
        DataclassValidator(ClosureInformationInput),
        Default(UnsetValue),
    )
    overallPeriod: OverallPeriodInput = DataclassValidator(OverallPeriodInput)
    afacOperatingHoursExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    afacOperatingHoursSpecificationExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
