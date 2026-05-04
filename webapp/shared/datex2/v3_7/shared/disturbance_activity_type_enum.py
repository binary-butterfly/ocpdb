"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class DisturbanceActivityTypeEnum(Enum):
    AIRRAID = 'airRaid'
    ALTERCATIONOFVEHICLEOCCUPANTS = 'altercationOfVehicleOccupants'
    ASSAULT = 'assault'
    ASSETDESTRUCTION = 'assetDestruction'
    ATTACK = 'attack'
    ATTACKONVEHICLE = 'attackOnVehicle'
    BLOCKADEORBARRIER = 'blockadeOrBarrier'
    BOMBALERT = 'bombAlert'
    CROWD = 'crowd'
    DEMONSTRATION = 'demonstration'
    EVACUATION = 'evacuation'
    FILTERBLOCKADE = 'filterBlockade'
    GOSLOWOPERATION = 'goSlowOperation'
    GUNFIREONROADWAY = 'gunfireOnRoadway'
    ILLVEHICLEOCCUPANTS = 'illVehicleOccupants'
    MARCH = 'march'
    PEOPLETHROWINGOBJECTSONTHEROAD = 'peopleThrowingObjectsOnTheRoad'
    PUBLICDISTURBANCE = 'publicDisturbance'
    RADIOACTIVELEAKALERT = 'radioactiveLeakAlert'
    RIOT = 'riot'
    SABOTAGE = 'sabotage'
    SECURITYALERT = 'securityAlert'
    SECURITYINCIDENT = 'securityIncident'
    SIGHTSEERSOBSTRUCTINGACCESS = 'sightseersObstructingAccess'
    STRIKE = 'strike'
    TERRORISTINCIDENT = 'terroristIncident'
    THEFT = 'theft'
    TOXICCLOUDALERT = 'toxicCloudAlert'
    UNSPECIFIEDALERT = 'unspecifiedAlert'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
