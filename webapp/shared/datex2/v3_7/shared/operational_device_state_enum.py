"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class OperationalDeviceStateEnum(Enum):
    MAINTENANCEMODE = 'maintenanceMode'
    ON = 'on'
    OFF = 'off'
    POWERSAFEMODE = 'powerSafeMode'
    SPECIALMODE = 'specialMode'
    TEMPORARILYDEACTIVATED = 'temporarilyDeactivated'
    PERMANENTLYDEACTIVATED = 'permanentlyDeactivated'
    UNKNOWN = 'unknown'
    EXTENDEDG = 'extendedG'
