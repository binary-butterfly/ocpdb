"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class OpenlrSideOfRoadEnum(Enum):
    ONROADORUNKNOWN = 'onRoadOrUnknown'
    RIGHT = 'right'
    LEFT = 'left'
    BOTH = 'both'
    EXTENDEDG = 'extendedG'
