"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class DedicatedUsageEnum(Enum):
    ENERGYINFORMATION = 'energyInformation'
    INSPECTIONAREA = 'inspectionArea'
    LANECONTROLSYSTEM = 'laneControlSystem'
    PARKINGINFORMATION = 'parkingInformation'
    RAMPMETERING = 'rampMetering'
    TUNNELMANAGEMENT = 'tunnelManagement'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
