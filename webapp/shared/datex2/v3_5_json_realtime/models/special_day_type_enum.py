"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class SpecialDayTypeEnum(Enum):
    DAYBEFOREPUBLICHOLIDAY = 'dayBeforePublicHoliday'
    PUBLICHOLIDAY = 'publicHoliday'
    DAYFOLLOWINGPUBLICHOLIDAY = 'dayFollowingPublicHoliday'
    LONGWEEKENDDAY = 'longWeekendDay'
    INLIEUOFPUBLICHOLIDAY = 'inLieuOfPublicHoliday'
    SCHOOLDAY = 'schoolDay'
    SCHOOLHOLIDAYS = 'schoolHolidays'
    PUBLICEVENTDAY = 'publicEventDay'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
