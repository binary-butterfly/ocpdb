"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class AccessibilityEnum(Enum):
    BARRIERFREEACCESSIBLE = 'barrierFreeAccessible'
    DISABILITYACCESSIBLE = 'disabilityAccessible'
    WHEELCHAIRACCESSIBLE = 'wheelChairAccessible'
    DISABILITYFACILITIES = 'disabilityFacilities'
    ORIENTATIONSYSTEMFORBLINDPEOPLE = 'orientationSystemForBlindPeople'
    MARKING = 'marking'
    NONE = 'none'
    UNKNOWN = 'unknown'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
