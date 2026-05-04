"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class ReroutingAdviceTypeEnum(Enum):
    DONOTFOLLOWDIVERSIONSIGNS = 'doNotFollowDiversionSigns'
    DONOTUSEENTRY = 'doNotUseEntry'
    DONOTUSEEXIT = 'doNotUseExit'
    DONOTUSEINTERSECTIONORJUNCTION = 'doNotUseIntersectionOrJunction'
    FOLLOWDIVERSIONSIGNS = 'followDiversionSigns'
    FOLLOWLOCALDIVERSION = 'followLocalDiversion'
    FOLLOWSPECIALMARKERS = 'followSpecialMarkers'
    USEENTRY = 'useEntry'
    USEEXIT = 'useExit'
    USEINTERSECTIONORJUNCTION = 'useIntersectionOrJunction'
    EXTENDEDG = 'extendedG'
