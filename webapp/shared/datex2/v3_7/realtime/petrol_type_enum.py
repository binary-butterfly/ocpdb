"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class PetrolTypeEnum(Enum):
    ALL = 'all'
    OCTANE95 = 'octane95'
    OCTANE98 = 'octane98'
    LEADED = 'leaded'
    UNLEADED = 'unleaded'
    SUPERE5 = 'superE5'
    SUPERE10 = 'superE10'
    OTHER = 'other'
    UNKNOWN = 'unknown'
    EXTENDEDG = 'extendedG'
