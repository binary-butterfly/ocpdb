"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class WeatherRelatedRoadConditionTypeEnum(Enum):
    BLACKICE = 'blackIce'
    DEEPSNOW = 'deepSnow'
    DRY = 'dry'
    FREEZINGOFWETROADS = 'freezingOfWetRoads'
    FREEZINGPAVEMENTS = 'freezingPavements'
    FREEZINGRAIN = 'freezingRain'
    FRESHSNOW = 'freshSnow'
    GLAZE = 'glaze'
    ICE = 'ice'
    ICEBUILDUP = 'iceBuildUp'
    ICEWITHWHEELBARTRACKS = 'iceWithWheelBarTracks'
    ICYPATCHES = 'icyPatches'
    LOOSESNOW = 'looseSnow'
    MOIST = 'moist'
    NORMALWINTERCONDITIONSFORPEDESTRIANS = 'normalWinterConditionsForPedestrians'
    NOTDRY = 'notDry'
    PACKEDSNOW = 'packedSnow'
    RIME = 'rime'
    ROADSURFACEMELTING = 'roadSurfaceMelting'
    SLIPPERY = 'slippery'
    SLUSHONROAD = 'slushOnRoad'
    SLUSHSTRINGS = 'slushStrings'
    SNOW = 'snow'
    SNOWDRIFTS = 'snowDrifts'
    SNOWONPAVEMENT = 'snowOnPavement'
    WETANDICYROAD = 'wetAndIcyRoad'
    SNOWONTHEROAD = 'snowOnTheRoad'
    WETICYPAVEMENT = 'wetIcyPavement'
    STREAMINGWATER = 'streamingWater'
    SURFACEWATER = 'surfaceWater'
    WET = 'wet'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
