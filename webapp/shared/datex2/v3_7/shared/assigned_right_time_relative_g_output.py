"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .relative_offsets_output import RelativeOffsetsOutput
from .times_of_day_output import TimesOfDayOutput


@dataclass(kw_only=True)
class AssignedRightTimeRelativeGOutput:
    """
    Only one of the properties shall be used in an instance.
    """

    afacRelativeOffsets: RelativeOffsetsOutput | None = None
    afacTimesOfDay: TimesOfDayOutput | None = None
