"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class DirectionCompassEnum(Enum):
    EAST = 'east'
    EASTNORTHEAST = 'eastNorthEast'
    EASTSOUTHEAST = 'eastSouthEast'
    NORTH = 'north'
    NORTHEAST = 'northEast'
    NORTHNORTHEAST = 'northNorthEast'
    NORTHNORTHWEST = 'northNorthWest'
    NORTHWEST = 'northWest'
    SOUTH = 'south'
    SOUTHEAST = 'southEast'
    SOUTHSOUTHEAST = 'southSouthEast'
    SOUTHSOUTHWEST = 'southSouthWest'
    SOUTHWEST = 'southWest'
    WEST = 'west'
    WESTNORTHWEST = 'westNorthWest'
    WESTSOUTHWEST = 'westSouthWest'
    EXTENDEDG = 'extendedG'
