"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class ParkingSpaceOccupancyDetectionEnum(Enum):
    VISUAL = 'visual'
    ANPR = 'anpr'
    IMAGEANALYTICS = 'imageAnalytics'
    VIDEOANALYTICS = 'videoAnalytics'
    VIDEOSPACE = 'videoSpace'
    SPACESENSOR = 'spaceSensor'
    USERDECLARATION = 'userDeclaration'
    BALANCING = 'balancing'
    MODELBASED = 'modelBased'
    NONE = 'none'
    UNKNOWN = 'unknown'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
