"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class AmbientWarningTypeEnum(Enum):
    ACCOMPANIEDHORSESCROSSING = 'accompaniedHorsesCrossing'
    AIRFIELD = 'airfield'
    CATTLE = 'cattle'
    FALLINGROCKS = 'fallingRocks'
    INSUFFICIENTSTRUCTUREGAUGE = 'insufficientStructureGauge'
    LOOSEGRAVEL = 'looseGravel'
    MIGRATORYTOADCROSSING = 'migratoryToadCrossing'
    OTHERDANGER = 'otherDanger'
    PEDESTRIANCROSSING = 'pedestrianCrossing'
    POORVISIBILITY = 'poorVisibility'
    QUAYSIDEORRIVERBANK = 'quaysideOrRiverBank'
    RISKOFICE = 'riskOfIce'
    SIDEWINDSLEFT = 'sideWindsLeft'
    SIDEWINDSRIGHT = 'sideWindsRight'
    WILDANIMALSCROSSING = 'wildAnimalsCrossing'
    EXTENDEDG = 'extendedG'
