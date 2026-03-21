"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, StringValidator

from .extension_type_g_input import ExtensionTypeGInput


@validataclass
class TimePeriodOfDayInput(ValidataclassMixin):
    """
    Specification of a continuous period of time within a 24 hour period.
    """

    startTimeOfPeriod: str = StringValidator()
    endTimeOfPeriod: str = StringValidator()
    comTimePeriodOfDayExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
