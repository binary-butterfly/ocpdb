"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class ParkingOccupancyEnum(Enum):
    EXPECTCARPARKTOBEFULL = 'expectCarParkToBeFull'
    PERCENTAGE10 = 'percentage10'
    PERCENTAGE20 = 'percentage20'
    PERCENTAGE30 = 'percentage30'
    PERCENTAGE40 = 'percentage40'
    PERCENTAGE50 = 'percentage50'
    PERCENTAGE60 = 'percentage60'
    PERCENTAGE70 = 'percentage70'
    PERCENTAGE80 = 'percentage80'
    PERCENTAGE90 = 'percentage90'
    FULL = 'full'
    UNKNOWN = 'unknown'
    EXTENDEDG = 'extendedG'
