"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class ParkingOccupancyTrendEnum(Enum):
    DECREASING = 'decreasing'
    INCREASING = 'increasing'
    STABLE = 'stable'
    INCREASINGQUICKLY = 'increasingQuickly'
    INCREASINGSLOWLY = 'increasingSlowly'
    DECREASINGQUICKLY = 'decreasingQuickly'
    DECREASINGSLOWLY = 'decreasingSlowly'
    UNKNOWN = 'unknown'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
