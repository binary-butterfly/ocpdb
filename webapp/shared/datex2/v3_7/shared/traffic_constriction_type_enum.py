"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class TrafficConstrictionTypeEnum(Enum):
    CARRIAGEWAYBLOCKED = 'carriagewayBlocked'
    CARRIAGEWAYPARTIALLYOBSTRUCTED = 'carriagewayPartiallyObstructed'
    LANESBLOCKED = 'lanesBlocked'
    LANESPARTIALLYOBSTRUCTED = 'lanesPartiallyObstructed'
    ROADBLOCKED = 'roadBlocked'
    ROADPARTIALLYOBSTRUCTED = 'roadPartiallyObstructed'
    EXTENDEDG = 'extendedG'
