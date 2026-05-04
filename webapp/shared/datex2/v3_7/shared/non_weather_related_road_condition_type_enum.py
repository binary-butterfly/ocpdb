"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class NonWeatherRelatedRoadConditionTypeEnum(Enum):
    DIESELONROAD = 'dieselOnRoad'
    LEAVESONROAD = 'leavesOnRoad'
    LOOSECHIPPINGS = 'looseChippings'
    LOOSESANDONROAD = 'looseSandOnRoad'
    MUDONROAD = 'mudOnRoad'
    OILONROAD = 'oilOnRoad'
    PETROLONROAD = 'petrolOnRoad'
    ROADMARKINGNOTPRESENT = 'roadMarkingNotPresent'
    ROADSURFACEINPOORCONDITION = 'roadSurfaceInPoorCondition'
    SLIPPERYROAD = 'slipperyRoad'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
