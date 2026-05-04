"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class BioethanolTypeEnum(Enum):
    SUPERE5 = 'superE5'
    SUPERE10 = 'superE10'
    E15 = 'e15'
    E85 = 'e85'
    E100 = 'e100'
    UNKNOWN = 'unknown'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
