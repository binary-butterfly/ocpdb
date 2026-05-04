"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class PriorityRuleTypeEnum(Enum):
    GIVEWAY = 'giveWay'
    GIVEWAYTOONCOMINGVEHICLES = 'giveWayToOncomingVehicles'
    GIVEWAYTORAIL = 'giveWayToRail'
    GIVEWAYTOSCHOOLCROSSINGPATROL = 'giveWayToSchoolCrossingPatrol'
    GIVEWAYTOTRAM = 'giveWayToTram'
    PRIORITYATNEXTJUNCTION = 'priorityAtNextJunction'
    PRIORITYOVERONCOMINGVEHICLES = 'priorityOverOncomingVehicles'
    PRIORITYROAD = 'priorityRoad'
    STOP = 'stop'
    EXTENDEDG = 'extendedG'
