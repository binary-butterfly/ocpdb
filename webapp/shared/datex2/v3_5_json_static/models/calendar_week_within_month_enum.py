"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class CalendarWeekWithinMonthEnum(Enum):
    FIRSTWEEK = 'firstWeek'
    SECONDWEEK = 'secondWeek'
    THIRDWEEK = 'thirdWeek'
    FOURTHWEEK = 'fourthWeek'
    FIFTHWEEK = 'fifthWeek'
    SIXTHWEEK = 'sixthWeek'
    LASTWEEK = 'lastWeek'
    EXTENDEDG = 'extendedG'
