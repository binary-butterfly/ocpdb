"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class PrecipitationTypeEnum(Enum):
    CLEARICE = 'clearIce'
    DEW = 'dew'
    DIAMONDDUST = 'diamondDust'
    DRIZZLE = 'drizzle'
    FREEZINGRAIN = 'freezingRain'
    GLAZE = 'glaze'
    HAIL = 'hail'
    HARDRIME = 'hardRime'
    HOARFROST = 'hoarFrost'
    ICECRYSTALS = 'iceCrystals'
    ICEPELLETS = 'icePellets'
    LIQUIDFREEZING = 'liquidFreezing'
    LIQUIDNOTFREEZING = 'liquidNotFreezing'
    NOPRECIPITATION = 'noPrecipitation'
    RAIN = 'rain'
    RIME = 'rime'
    SLEET = 'sleet'
    SMALLHAIL = 'smallHail'
    SNOW = 'snow'
    SNOWGRAINS = 'snowGrains'
    SNOWPELLETS = 'snowPellets'
    SOFTRIME = 'softRime'
    SOLID = 'solid'
    WETSNOW = 'wetSnow'
    WHITEDEV = 'whiteDev'
    UNKNOWN = 'unknown'
    EXTENDEDG = 'extendedG'
