"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class InfrastructureDamageTypeEnum(Enum):
    BURSTPIPE = 'burstPipe'
    BURSTWATERMAIN = 'burstWaterMain'
    COLLAPSEDSEWER = 'collapsedSewer'
    DAMAGEDBRIDGE = 'damagedBridge'
    DAMAGEDCRASHBARRIER = 'damagedCrashBarrier'
    DAMAGEDFLYOVER = 'damagedFlyover'
    DAMAGEDGALLERY = 'damagedGallery'
    DAMAGEDGANTRY = 'damagedGantry'
    DAMAGEDROADSURFACE = 'damagedRoadSurface'
    DAMAGEDTUNNEL = 'damagedTunnel'
    DAMAGEDVIADUCT = 'damagedViaduct'
    FALLENPOWERCABLES = 'fallenPowerCables'
    GASLEAK = 'gasLeak'
    WEAKBRIDGE = 'weakBridge'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
