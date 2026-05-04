"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class ParkingPlaceStatusEnum(Enum):
    FULL = 'full'
    FULLATENTRANCE = 'fullAtEntrance'
    SPACESAVAILABLE = 'spacesAvailable'
    ALMOSTFULL = 'almostFull'
    OVERCROWDING = 'overcrowding'
    OVERCROWDINGLEVEL1 = 'overcrowdingLevel1'
    OVERCROWDINGLEVEL2 = 'overcrowdingLevel2'
    NOOVERCROWDING = 'noOvercrowding'
    UNKNOWN = 'unknown'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
