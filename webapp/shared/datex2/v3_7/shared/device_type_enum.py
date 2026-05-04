"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class DeviceTypeEnum(Enum):
    ACCESSCONTROL = 'accessControl'
    CAMERA = 'camera'
    FIREDETECTION = 'fireDetection'
    FIREFIGHTINGDEVICE = 'firefightingDevice'
    ITSSTATION = 'itsStation'
    LIGHTING = 'lighting'
    METEOROLOGICAL = 'meteorological'
    ROADSIDETELEPHONE = 'roadsideTelephone'
    TOLLINGDEVICE = 'tollingDevice'
    TRAFFICDETECTOR = 'trafficDetector'
    VENTILATION = 'ventilation'
    PARKINGGUIDANCE = 'parkingGuidance'
    PARKINGMANAGEMENT = 'parkingManagement'
    ROADSIDEEQUIPMENT = 'roadsideEquipment'
    TRAFFICSIGNAL = 'trafficSignal'
    TRANSPORTLINK = 'transportLink'
    TRANSPORTROUTE = 'transportRoute'
    TUNNEL = 'tunnel'
    VEHICLE = 'vehicle'
    VMS = 'vms'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
