"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class CauseTypeEnum(Enum):
    ABNORMALTRAFFIC = 'abnormalTraffic'
    ACCIDENT = 'accident'
    ANIMALPRESENCE = 'animalPresence'
    AUTHORITYOPERATION = 'authorityOperation'
    CONSTRUCTIONWORK = 'constructionWork'
    DISTURBANCE = 'disturbance'
    DRIVINGCONDITIONS = 'drivingConditions'
    ENVIRONMENTALOBSTRUCTION = 'environmentalObstruction'
    EQUIPMENTORSYSTEMFAULT = 'equipmentOrSystemFault'
    INFRASTRUCTUREDAMAGEOBSTRUCTION = 'infrastructureDamageObstruction'
    INSTRUCTIONTOROADUSERS = 'instructionToRoadUsers'
    NETWORKMANAGEMENT = 'networkManagement'
    NONWEATHERRELATEDROADCONDITIONS = 'nonWeatherRelatedRoadConditions'
    OBSTRUCTION = 'obstruction'
    POORENVIRONMENT = 'poorEnvironment'
    PUBLICEVENT = 'publicEvent'
    REROUTING = 'rerouting'
    ROADMAINTENANCE = 'roadMaintenance'
    ROADOPERATORSERVICEDISRUPTION = 'roadOperatorServiceDisruption'
    ROADORCARRIAGEWAYORLANEMANAGEMENT = 'roadOrCarriagewayOrLaneManagement'
    ROADSIDEASSISTANCE = 'roadsideAssistance'
    ROADSIDESERVICEDISRUPTION = 'roadsideServiceDisruption'
    SPEEDMANAGEMENT = 'speedManagement'
    TRANSITSERVICEDISRUPTION = 'transitServiceDisruption'
    VEHICLEOBSTRUCTION = 'vehicleObstruction'
    WEATHERRELATEDROADCONDITIONS = 'weatherRelatedRoadConditions'
    WINTEREQUIPMENTMANAGEMENT = 'winterEquipmentManagement'
    EARLIEREVENT = 'earlierEvent'
    EARLIERINCIDENT = 'earlierIncident'
    HOLIDAYTRAFFIC = 'holidayTraffic'
    PROBLEMSATBORDERPOST = 'problemsAtBorderPost'
    PROBLEMSATCUSTOMPOST = 'problemsAtCustomPost'
    PROBLEMSONLOCALROADS = 'problemsOnLocalRoads'
    ROADSIDEEVENT = 'roadsideEvent'
    RUBBERNECKING = 'rubberNecking'
    TECHNICALPROBLEMS = 'technicalProblems'
    VANDALISM = 'vandalism'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
