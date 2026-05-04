"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class TravelTimeTypeEnum(Enum):
    BEST = 'best'
    ESTIMATED = 'estimated'
    INSTANTANEOUS = 'instantaneous'
    RECONSTITUTED = 'reconstituted'
    PREDICTOR = 'predictor'
    PROFILE = 'profile'
    SUM = 'sum'
    EXTENDEDG = 'extendedG'
