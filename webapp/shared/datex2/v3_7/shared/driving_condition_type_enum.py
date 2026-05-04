"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class DrivingConditionTypeEnum(Enum):
    IMPOSSIBLE = 'impossible'
    HAZARDOUS = 'hazardous'
    NORMAL = 'normal'
    PASSABLEWITHCARE = 'passableWithCare'
    UNKNOWN = 'unknown'
    VERYHAZARDOUS = 'veryHazardous'
    WINTERCONDITIONS = 'winterConditions'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
