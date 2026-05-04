"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class DelayBandEnum(Enum):
    NEGLIGIBLE = 'negligible'
    UPTOTENMINUTES = 'upToTenMinutes'
    BETWEENTENMINUTESANDTHIRTYMINUTES = 'betweenTenMinutesAndThirtyMinutes'
    BETWEENTHIRTYMINUTESANDONEHOUR = 'betweenThirtyMinutesAndOneHour'
    BETWEENONEHOURANDTHREEHOURS = 'betweenOneHourAndThreeHours'
    BETWEENTHREEHOURSANDSIXHOURS = 'betweenThreeHoursAndSixHours'
    LONGERTHANSIXHOURS = 'longerThanSixHours'
    EXTENDEDG = 'extendedG'
