"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class SubjectTypeOfWorksEnum(Enum):
    BRIDGE = 'bridge'
    BURIEDCABLES = 'buriedCables'
    BURIEDSERVICES = 'buriedServices'
    CRASHBARRIER = 'crashBarrier'
    CYCLETRACK = 'cycleTrack'
    FOOTPATH = 'footpath'
    GALLERY = 'gallery'
    GANTRY = 'gantry'
    GASMAINWORK = 'gasMainWork'
    HEATINGPIPE = 'heatingPipe'
    INTERCHANGE = 'interchange'
    JUNCTION = 'junction'
    LEVELCROSSING = 'levelCrossing'
    LIGHTINGSYSTEM = 'lightingSystem'
    LOCK = 'lock'
    MEASUREMENTEQUIPMENT = 'measurementEquipment'
    METRO = 'metro'
    NOISEPROTECTION = 'noiseProtection'
    PARKING = 'parking'
    PUBLICTRANSPORTINFRASTRUCTURE = 'publicTransportInfrastructure'
    PUBLICTRANSPORTSTOP = 'publicTransportStop'
    ROAD = 'road'
    ROADSIGNS = 'roadSigns'
    ROADSIDEDRAINS = 'roadsideDrains'
    ROADSIDEEMBANKMENT = 'roadsideEmbankment'
    ROADSIDEEQUIPMENT = 'roadsideEquipment'
    ROUNDABOUT = 'roundabout'
    SEWER = 'sewer'
    STREETPARKING = 'streetParking'
    TOLLGATE = 'tollGate'
    TRAFFICSIGNALS = 'trafficSignals'
    TUNNEL = 'tunnel'
    WATERBANK = 'waterBank'
    WATERMAIN = 'waterMain'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
