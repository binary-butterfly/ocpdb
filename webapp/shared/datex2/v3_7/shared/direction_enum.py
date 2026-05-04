"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class DirectionEnum(Enum):
    ALIGNED = 'aligned'
    ALLDIRECTIONS = 'allDirections'
    ANTICLOCKWISE = 'anticlockwise'
    BOTHWAYS = 'bothWays'
    CLOCKWISE = 'clockwise'
    INNERRING = 'innerRing'
    OUTERRING = 'outerRing'
    EASTBOUND = 'eastBound'
    NORTHBOUND = 'northBound'
    NORTHEASTBOUND = 'northEastBound'
    NORTHWESTBOUND = 'northWestBound'
    SOUTHBOUND = 'southBound'
    SOUTHEASTBOUND = 'southEastBound'
    SOUTHWESTBOUND = 'southWestBound'
    WESTBOUND = 'westBound'
    INBOUNDTOWARDSTOWN = 'inboundTowardsTown'
    OUTBOUNDFROMTOWN = 'outboundFromTown'
    OPPOSITE = 'opposite'
    UNKNOWN = 'unknown'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
