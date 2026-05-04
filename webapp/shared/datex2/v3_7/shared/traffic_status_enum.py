"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class TrafficStatusEnum(Enum):
    STATIONARY = 'stationary'
    QUEUING = 'queuing'
    SLOW = 'slow'
    HEAVY = 'heavy'
    UNSPECIFIEDABNORMAL = 'unspecifiedAbnormal'
    FREEFLOW = 'freeFlow'
    UNKNOWN = 'unknown'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
