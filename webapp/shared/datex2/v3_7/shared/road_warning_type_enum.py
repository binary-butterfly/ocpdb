"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class RoadWarningTypeEnum(Enum):
    ACCIDENT = 'accident'
    BENDTOLEFT = 'bendToLeft'
    BENDTORIGHT = 'bendToRight'
    CROSSROADSWITHPRIORITYFROMRIGHT = 'crossroadsWithPriorityFromRight'
    DOUBLEBENDFIRSTTOLEFT = 'doubleBendFirstToLeft'
    DOUBLEBENDFIRSTTORIGHT = 'doubleBendFirstToRight'
    LATERALSTEP = 'lateralStep'
    LIGHTSIGNALS = 'lightSignals'
    OBSTACLEONTHEROAD = 'obstacleOnTheRoad'
    ROADDIP = 'roadDip'
    ROADHUMP = 'roadHump'
    ROADNARROWSBOTHSIDES = 'roadNarrowsBothSides'
    ROADNARROWSLEFT = 'roadNarrowsLeft'
    ROADNARROWSRIGHT = 'roadNarrowsRight'
    ROADWORKS = 'roadWorks'
    ROUNDABOUTANTICLOCKWISE = 'roundaboutAntiClockwise'
    ROUNDABOUTCLOCKWISE = 'roundaboutClockwise'
    SLIPPERYROAD = 'slipperyRoad'
    SWINGBRIDGE = 'swingBridge'
    UNEVENROAD = 'unevenRoad'
    EXTENDEDG = 'extendedG'
