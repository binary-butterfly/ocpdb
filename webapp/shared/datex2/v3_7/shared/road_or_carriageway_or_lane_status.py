"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class RoadOrCarriagewayOrLaneStatus(Enum):
    CLOSED = 'closed'
    DEVIATEDTOHARDSHOULDER = 'deviatedToHardShoulder'
    DEVIATEDTOLEFT = 'deviatedToLeft'
    DEVIATEDTOOTHERCARRIAGEWAY = 'deviatedToOtherCarriageway'
    DEVIATEDTORIGHT = 'deviatedToRight'
    MERGEDTOLEFT = 'mergedToLeft'
    MERGEDTORIGHT = 'mergedToRight'
    OPEN = 'open'
    EXTENDEDG = 'extendedG'
