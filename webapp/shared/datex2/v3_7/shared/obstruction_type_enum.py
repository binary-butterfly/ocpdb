"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class ObstructionTypeEnum(Enum):
    AIRCRASH = 'airCrash'
    CHILDRENONROADWAY = 'childrenOnRoadway'
    CLEARANCEWORK = 'clearanceWork'
    CRANEOPERATING = 'craneOperating'
    CYCLISTSONROADWAY = 'cyclistsOnRoadway'
    DEBRIS = 'debris'
    EXPLOSION = 'explosion'
    EXPLOSIONHAZARD = 'explosionHazard'
    HAZARDSONTHEROAD = 'hazardsOnTheRoad'
    INCIDENT = 'incident'
    INDUSTRIALACCIDENT = 'industrialAccident'
    OBJECTONTHEROAD = 'objectOnTheRoad'
    OBJECTSFALLINGFROMMOVINGVEHICLE = 'objectsFallingFromMovingVehicle'
    OBSTRUCTIONONTHEROAD = 'obstructionOnTheRoad'
    PEOPLEONROADWAY = 'peopleOnRoadway'
    RAILCRASH = 'railCrash'
    RESCUEANDRECOVERYWORK = 'rescueAndRecoveryWork'
    SEVEREFROSTDAMAGEDROADWAY = 'severeFrostDamagedRoadway'
    SHEDLOAD = 'shedLoad'
    SNOWANDICEDEBRIS = 'snowAndIceDebris'
    SPILLAGEOCCURRINGFROMMOVINGVEHICLE = 'spillageOccurringFromMovingVehicle'
    SPILLAGEONTHEROAD = 'spillageOnTheRoad'
    UNPROTECTEDACCIDENTAREA = 'unprotectedAccidentArea'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
