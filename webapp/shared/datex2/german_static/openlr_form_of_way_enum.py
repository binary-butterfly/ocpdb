"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class OpenlrFormOfWayEnum(Enum):
    UNDEFINED = 'undefined'
    MOTORWAY = 'motorway'
    MULTIPLECARRIAGEWAY = 'multipleCarriageway'
    SINGLECARRIAGEWAY = 'singleCarriageway'
    ROUNDABOUT = 'roundabout'
    SLIPROAD = 'slipRoad'
    TRAFFICSQUARE = 'trafficSquare'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
