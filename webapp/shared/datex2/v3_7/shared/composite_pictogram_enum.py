"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class CompositePictogramEnum(Enum):
    CONDITIONONCURRENTSECTIONAFTERNEXTEXIT = 'conditionOnCurrentSectionAfterNextExit'
    CONDITIONATNEXTEXIT = 'conditionAtNextExit'
    CONDITIONONCURRENTSECTIONAFTERSECONDTEXIT = 'conditionOnCurrentSectionAfterSecondtExit'
    CONDITIONATSECONDEXIT = 'conditionAtSecondExit'
    RESTRICTIONONCURRENTSECTIONAFTERNEXTEXIT = 'restrictionOnCurrentSectionAfterNextExit'
    RESTRICTIONATNEXTEXIT = 'restrictionAtNextExit'
    RESTRICTIONONCURRENTSECTIONAFTERSECONDEXIT = 'restrictionOnCurrentSectionAfterSecondExit'
    RESTRICTIONATSECONDTEXIT = 'restrictionAtSecondtExit'
    EXTENDEDG = 'extendedG'
