"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import ValidataclassMixin, validataclass
from validataclass.validators import DataclassValidator

from .applicable_days_within_month_enum_g_input import ApplicableDaysWithinMonthEnumGInput


@validataclass
class DayWeekMonthExtendedInput(ValidataclassMixin):
    """
    Extension of class DayWeekMonth.
    """

    applicableDaysWithinMonth: ApplicableDaysWithinMonthEnumGInput = DataclassValidator(
        ApplicableDaysWithinMonthEnumGInput
    )
