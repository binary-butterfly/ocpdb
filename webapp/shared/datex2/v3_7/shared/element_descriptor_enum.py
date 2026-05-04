"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class ElementDescriptorEnum(Enum):
    FLOORORLEVEL = 'floorOrLevel'
    ROW = 'row'
    STREET = 'street'
    BUILDING = 'building'
    STATISTICSONLY = 'statisticsOnly'
    MIXEDUSAGE = 'mixedUsage'
    SINGLEPARAMETERS = 'singleParameters'
    LOGICALSTRUCTURE = 'logicalStructure'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
