"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class OrganicGasTypeEnum(Enum):
    ALL = 'all'
    CNG = 'cng'
    LNG = 'lng'
    LPG = 'lpg'
    BIOGAS = 'biogas'
    OTHER = 'other'
    UNKNOWN = 'unknown'
    EXTENDEDG = 'extendedG'
