"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class DirectionRestrictionTypeEnum(Enum):
    AHEADONLY = 'aheadOnly'
    KEEPLEFT = 'keepLeft'
    KEEPRIGHT = 'keepRight'
    NOLEFTTURN = 'noLeftTurn'
    NOREVERSING = 'noReversing'
    NORIGHTTURN = 'noRightTurn'
    NOTHROUGHROAD = 'noThroughRoad'
    NOUTURN = 'noUTurn'
    ONEWAYTRAFFIC = 'oneWayTraffic'
    PASSEITHERSIDE = 'passEitherSide'
    ROUNDABOUT = 'roundabout'
    STRAIGHTAHEADORTURNLEFT = 'straightAheadOrTurnLeft'
    STRAIGHTAHEADORTURNRIGHT = 'straightAheadOrTurnRight'
    TURNLEFT = 'turnLeft'
    TURNLEFTAHEAD = 'turnLeftAhead'
    TURNLEFTORTURNRIGHT = 'turnLeftOrTurnRight'
    TURNRIGHT = 'turnRight'
    TURNRIGHTAHEAD = 'turnRightAhead'
    EXTENDEDG = 'extendedG'
