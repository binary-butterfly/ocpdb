"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class CapacityManagementMeasureEnum(Enum):
    ACCESSMEASURES = 'accessMeasures'
    CAPACITYINCREASE = 'capacityIncrease'
    CAPACITYREDUCTION = 'capacityReduction'
    INFLOWREDUCTION = 'inflowReduction'
    OUTFLOWINCREASE = 'outflowIncrease'
    PARKINGMEASURES = 'parkingMeasures'
    SIGNALMEASURES = 'signalMeasures'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
