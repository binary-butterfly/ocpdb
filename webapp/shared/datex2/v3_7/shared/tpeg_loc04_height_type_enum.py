"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class TpegLoc04HeightTypeEnum(Enum):
    ABOVE = 'above'
    ABOVESEALEVEL = 'aboveSeaLevel'
    ABOVESTREETLEVEL = 'aboveStreetLevel'
    AT = 'at'
    ATSEALEVEL = 'atSeaLevel'
    ATSTREETLEVEL = 'atStreetLevel'
    BELOW = 'below'
    BELOWSEALEVEL = 'belowSeaLevel'
    BELOWSTREETLEVEL = 'belowStreetLevel'
    UNDEFINED = 'undefined'
    UNKNOWN = 'unknown'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
