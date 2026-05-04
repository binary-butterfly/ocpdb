"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class TrafficAheadTypeEnum(Enum):
    BUSCROSSING = 'busCrossing'
    CHILDREN = 'children'
    CYCLEROUTE = 'cycleRoute'
    LEVELCROSSING = 'levelCrossing'
    LEVELCROSSINGWITHGATE = 'levelCrossingWithGate'
    PEDESTRIANCROSSING = 'pedestrianCrossing'
    RIDINGPATH = 'ridingPath'
    TRAFFICQUEUES = 'trafficQueues'
    TRAMSCROSSINGAHEAD = 'tramsCrossingAhead'
    TWOWAYTRAFFIC = 'twoWayTraffic'
    EXTENDEDG = 'extendedG'
