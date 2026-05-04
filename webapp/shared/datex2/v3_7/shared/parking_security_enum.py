"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class ParkingSecurityEnum(Enum):
    SOCIALCONTROL = 'socialControl'
    SECURITYSTAFF = 'securityStaff'
    EXTERNALSECURITY = 'externalSecurity'
    CCTV = 'cctv'
    DOG = 'dog'
    GUARD24HOURS = 'guard24hours'
    LIGHTING = 'lighting'
    FLOODLIGHT = 'floodLight'
    FENCES = 'fences'
    AREASEPERATEDFROMSURROUNDINGS = 'areaSeperatedFromSurroundings'
    NONE = 'none'
    UNKNOWN = 'unknown'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
