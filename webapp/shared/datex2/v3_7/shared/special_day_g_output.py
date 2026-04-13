"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .public_holiday_output import PublicHolidayOutput
from .special_day_output import SpecialDayOutput


@dataclass(kw_only=True)
class SpecialDayGOutput:
    """
    Only one of the properties shall be used in an instance.
    """

    comSpecialDay: SpecialDayOutput | None = None
    comPublicHoliday: PublicHolidayOutput | None = None
