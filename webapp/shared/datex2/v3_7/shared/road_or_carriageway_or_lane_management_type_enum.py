"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class RoadOrCarriagewayOrLaneManagementTypeEnum(Enum):
    CARPOOLLANEINOPERATION = 'carPoolLaneInOperation'
    CARRIAGEWAYCLOSURES = 'carriagewayClosures'
    CLEARALANEFOREMERGENCYVEHICLES = 'clearALaneForEmergencyVehicles'
    CLEARALANEFORSNOWPLOUGHSANDGRITTINGVEHICLES = 'clearALaneForSnowploughsAndGrittingVehicles'
    CLOSEDPERMANENTLYFORTHEWINTER = 'closedPermanentlyForTheWinter'
    CONTRAFLOW = 'contraflow'
    DONOTUSESPECIFIEDLANESORCARRIAGEWAYS = 'doNotUseSpecifiedLanesOrCarriageways'
    HARDSHOULDERRUNNINGINOPERATION = 'hardShoulderRunningInOperation'
    HARDSHOULDERRUNNINGNOTINOPERATION = 'hardShoulderRunningNotInOperation'
    HEIGHTRESTRICTIONINOPERATION = 'heightRestrictionInOperation'
    INTERMITTENTSHORTTERMCLOSURES = 'intermittentShortTermClosures'
    KEEPTOTHELEFT = 'keepToTheLeft'
    KEEPTOTHERIGHT = 'keepToTheRight'
    LANECLOSURES = 'laneClosures'
    LANESDEVIATED = 'lanesDeviated'
    NARROWLANES = 'narrowLanes'
    NEWROADWORKSLAYOUT = 'newRoadworksLayout'
    OVERNIGHTCLOSURES = 'overnightClosures'
    ROADCLEARED = 'roadCleared'
    ROADCLOSED = 'roadClosed'
    ROLLINGROADBLOCK = 'rollingRoadBlock'
    RUSHHOURLANEINOPERATION = 'rushHourLaneInOperation'
    SINGLEALTERNATELINETRAFFIC = 'singleAlternateLineTraffic'
    TIDALFLOWLANEINOPERATION = 'tidalFlowLaneInOperation'
    TURNAROUNDINOPERATION = 'turnAroundInOperation'
    USEOFSPECIFIEDLANESORCARRIAGEWAYSALLOWED = 'useOfSpecifiedLanesOrCarriagewaysAllowed'
    USESPECIFIEDLANESORCARRIAGEWAYS = 'useSpecifiedLanesOrCarriageways'
    VEHICLESTORAGEINOPERATION = 'vehicleStorageInOperation'
    WEIGHTRESTRICTIONINOPERATION = 'weightRestrictionInOperation'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
