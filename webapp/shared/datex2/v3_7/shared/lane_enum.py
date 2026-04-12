"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class LaneEnum(Enum):
    ALLLANESCOMPLETECARRIAGEWAY = 'allLanesCompleteCarriageway'
    BUSLANE = 'busLane'
    BUSSTOP = 'busStop'
    CARPOOLLANE = 'carPoolLane'
    CENTRALRESERVATION = 'centralReservation'
    CRAWLERLANE = 'crawlerLane'
    CYCLELANE = 'cycleLane'
    EMERGENCYLANE = 'emergencyLane'
    ESCAPELANE = 'escapeLane'
    EXPRESSLANE = 'expressLane'
    HARDSHOULDER = 'hardShoulder'
    HEAVYVEHICLELANE = 'heavyVehicleLane'
    LAYBY = 'layBy'
    LEFTHANDTURNINGLANE = 'leftHandTurningLane'
    LEFTLANE = 'leftLane'
    LOCALTRAFFICLANE = 'localTrafficLane'
    MIDDLELANE = 'middleLane'
    OVERTAKINGLANE = 'overtakingLane'
    RIGHTHANDTURNINGLANE = 'rightHandTurningLane'
    RIGHTLANE = 'rightLane'
    RUSHHOURLANE = 'rushHourLane'
    SETDOWNAREA = 'setDownArea'
    SLOWVEHICLELANE = 'slowVehicleLane'
    THROUGHTRAFFICLANE = 'throughTrafficLane'
    TIDALFLOWLANE = 'tidalFlowLane'
    TURNINGLANE = 'turningLane'
    VERGE = 'verge'
    EXTENDEDG = 'extendedG'
