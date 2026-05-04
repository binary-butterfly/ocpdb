"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class GeneralNetworkManagementTypeEnum(Enum):
    BRIDGESWINGINOPERATION = 'bridgeSwingInOperation'
    CONVOYSERVICE = 'convoyService'
    OBSTACLESIGNALLING = 'obstacleSignalling'
    RAMPMETERINGINOPERATION = 'rampMeteringInOperation'
    TEMPORARYTRAFFICLIGHTS = 'temporaryTrafficLights'
    TOLLGATESOPEN = 'tollGatesOpen'
    TRAFFICBEINGMANUALLYDIRECTED = 'trafficBeingManuallyDirected'
    TRAFFICHELD = 'trafficHeld'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
