"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class SpeedManagementTypeEnum(Enum):
    ACTIVESPEEDCONTROLINOPERATION = 'activeSpeedControlInOperation'
    DONOTSLOWDOWNUNNECESSARILY = 'doNotSlowdownUnnecessarily'
    OBSERVESPEEDLIMIT = 'observeSpeedLimit'
    POLICESPEEDCHECKSINOPERATION = 'policeSpeedChecksInOperation'
    REDUCEYOURSPEED = 'reduceYourSpeed'
    SPEEDRESTRICTIONINOPERATION = 'speedRestrictionInOperation'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
