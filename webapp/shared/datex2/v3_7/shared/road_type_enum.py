"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class RoadTypeEnum(Enum):
    MOTORWAY = 'motorway'
    TRUNKROAD = 'trunkRoad'
    MAINROAD = 'mainRoad'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
