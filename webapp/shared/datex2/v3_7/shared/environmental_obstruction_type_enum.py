"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class EnvironmentalObstructionTypeEnum(Enum):
    AVALANCHES = 'avalanches'
    EARTHQUAKEDAMAGE = 'earthquakeDamage'
    FALLENTREES = 'fallenTrees'
    FALLINGICE = 'fallingIce'
    FALLINGLIGHTICEORSNOW = 'fallingLightIceOrSnow'
    FLASHFLOODS = 'flashFloods'
    FLOODING = 'flooding'
    FORESTFIRE = 'forestFire'
    GRASSFIRE = 'grassFire'
    LANDSLIPS = 'landslips'
    MUDSLIDE = 'mudSlide'
    SEWEROVERFLOW = 'sewerOverflow'
    ROCKFALLS = 'rockfalls'
    SERIOUSFIRE = 'seriousFire'
    SMOKEORFUMES = 'smokeOrFumes'
    STORMDAMAGE = 'stormDamage'
    SUBSIDENCE = 'subsidence'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
