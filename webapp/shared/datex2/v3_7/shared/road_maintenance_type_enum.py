"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class RoadMaintenanceTypeEnum(Enum):
    ACCIDENTREPAIRWORK = 'accidentRepairWork'
    CLEARANCEWORK = 'clearanceWork'
    CONTROLLEDAVALANCHE = 'controlledAvalanche'
    INSTALLATIONWORK = 'installationWork'
    GRASSCUTTINGWORK = 'grassCuttingWork'
    LITTERCLEARANCE = 'litterClearance'
    MAINTENANCEWORK = 'maintenanceWork'
    MAINTENANCEPEOPLEONROAD = 'maintenancePeopleOnRoad'
    OVERHEADWORKS = 'overheadWorks'
    REPAIRWORK = 'repairWork'
    RESURFACINGWORK = 'resurfacingWork'
    ROADMARKINGWORK = 'roadMarkingWork'
    ROADSIDEWORK = 'roadsideWork'
    ROADWORKSCLEARANCE = 'roadworksClearance'
    ROADWORKS = 'roadworks'
    ROCKFALLPREVENTATIVEMAINTENANCE = 'rockFallPreventativeMaintenance'
    SALTINGINPROGRESS = 'saltingInProgress'
    SNOWPLOUGHSINUSE = 'snowploughsInUse'
    SWEEPINGOFROAD = 'sweepingOfRoad'
    TREEANDVEGETATIONCUTTINGWORK = 'treeAndVegetationCuttingWork'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
