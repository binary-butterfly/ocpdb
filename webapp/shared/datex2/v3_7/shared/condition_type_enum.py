"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class ConditionTypeEnum(Enum):
    ACCESSCONDITION = 'accessCondition'
    DRIVERCONDITION = 'driverCondition'
    LOCATIONCONDITION = 'locationCondition'
    NONVEHICULARROADUSERCONDITION = 'nonVehicularRoadUserCondition'
    OCCUPANTCONDITIONS = 'occupantConditions'
    OTHER = 'other'
    PERMITCONDITION = 'permitCondition'
    REGISTRATIONCONDITION = 'registrationCondition'
    RETROFITTINGCONDITION = 'retrofittingCondition'
    ROADCONDITION = 'roadCondition'
    STICKERCONDITION = 'stickerCondition'
    VALIDITYCONDITION = 'validityCondition'
    VEHICLECONDITION = 'vehicleCondition'
    EXTENDEDG = 'extendedG'
