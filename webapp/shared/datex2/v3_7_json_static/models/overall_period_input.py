"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator, StringValidator

from .extension_type_g_input import ExtensionTypeGInput
from .period_input import PeriodInput


@validataclass
class OverallPeriodInput(ValidataclassMixin):
    """
    A continuous or discontinuous period of validity defined by overall bounding start and end times and the possible intersection of valid periods (potentially recurring) with the complement of exception periods (also potentially recurring).
    """

    overallStartTime: str = StringValidator()
    overallEndTime: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    validPeriod: list[PeriodInput] | UnsetValueType = (
        ListValidator(DataclassValidator(PeriodInput)),
        Default(UnsetValue),
    )
    exceptionPeriod: list[PeriodInput] | UnsetValueType = (
        ListValidator(DataclassValidator(PeriodInput)),
        Default(UnsetValue),
    )
    comOverallPeriodExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
