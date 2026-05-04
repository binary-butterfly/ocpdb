"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class EquipmentOrSystemTypeEnum(Enum):
    ANPRCAMERAS = 'anprCameras'
    AUTOMATEDTOLLSYSTEM = 'automatedTollSystem'
    CCTVCAMERAS = 'cctvCameras'
    EMERGENCYROADSIDETELEPHONES = 'emergencyRoadsideTelephones'
    FIREDETECTIONEQUIPMENT = 'fireDetectionEquipment'
    GALLERYLIGHTS = 'galleryLights'
    LANECONTROLSIGNS = 'laneControlSigns'
    LEVELCROSSING = 'levelCrossing'
    MATRIXSIGNS = 'matrixSigns'
    RAMPCONTROLS = 'rampControls'
    ROADSIDECOMMUNICATIONSSYSTEM = 'roadsideCommunicationsSystem'
    ROADSIDEPOWERSYSTEM = 'roadsidePowerSystem'
    SPEEDCONTROLSIGNS = 'speedControlSigns'
    STREETLIGHTING = 'streetLighting'
    TEMPORARYTRAFFICLIGHTS = 'temporaryTrafficLights'
    TOLLGATES = 'tollGates'
    TRAFFICLIGHTSETS = 'trafficLightSets'
    TRAFFICSIGNALS = 'trafficSignals'
    TUNNELEMERGENCYPHONES = 'tunnelEmergencyPhones'
    TUNNELFIREFIGHTINGEQUIPMENT = 'tunnelFireFightingEquipment'
    TUNNELLIGHTS = 'tunnelLights'
    TUNNELMOBILECOMMUNICATION = 'tunnelMobileCommunication'
    TUNNELRADIOCOMMUNICATION = 'tunnelRadioCommunication'
    TUNNELSAFETYSYSTEM = 'tunnelSafetySystem'
    TUNNELVENTILATION = 'tunnelVentilation'
    VARIABLEMESSAGESIGNS = 'variableMessageSigns'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
