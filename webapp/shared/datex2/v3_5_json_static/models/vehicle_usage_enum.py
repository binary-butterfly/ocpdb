"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class VehicleUsageEnum(Enum):
    AGRICULTURAL = 'agricultural'
    CARSHARING = 'carSharing'
    CITYLOGISTICS = 'cityLogistics'
    COMMERCIAL = 'commercial'
    EMERGENCYSERVICES = 'emergencyServices'
    MILITARY = 'military'
    NONCOMMERCIAL = 'nonCommercial'
    PATROL = 'patrol'
    RECOVERYSERVICES = 'recoveryServices'
    ROADMAINTENANCEORCONSTRUCTION = 'roadMaintenanceOrConstruction'
    ROADOPERATOR = 'roadOperator'
    TAXI = 'taxi'
    EXTENDEDG = 'extendedG'
