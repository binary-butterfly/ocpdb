"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class CarriagewayEnum(Enum):
    CONNECTINGCARRIAGEWAY = 'connectingCarriageway'
    CYCLETRACK = 'cycleTrack'
    ENTRYSLIPROAD = 'entrySlipRoad'
    EXITSLIPROAD = 'exitSlipRoad'
    FLYOVER = 'flyover'
    FOOTPATH = 'footpath'
    LEFTHANDPARALLELCARRIAGEWAY = 'leftHandParallelCarriageway'
    LEFTHANDFEEDERROAD = 'leftHandFeederRoad'
    MAINCARRIAGEWAY = 'mainCarriageway'
    OPPOSITECARRIAGEWAY = 'oppositeCarriageway'
    PARALLELCARRIAGEWAY = 'parallelCarriageway'
    RIGHTHANDFEEDERROAD = 'rightHandFeederRoad'
    RIGHTHANDPARALLELCARRIAGEWAY = 'rightHandParallelCarriageway'
    ROUNDABOUT = 'roundabout'
    SERVICEROAD = 'serviceRoad'
    SLIPROADS = 'slipRoads'
    UNDERPASS = 'underpass'
    UNSPECIFIEDCARRIAGEWAY = 'unspecifiedCarriageway'
    EXTENDEDG = 'extendedG'
