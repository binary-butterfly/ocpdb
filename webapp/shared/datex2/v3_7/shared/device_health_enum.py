"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class DeviceHealthEnum(Enum):
    OK = 'ok'
    NOTOK = 'notOk'
    FUNCTIONALITYPARTLYOK = 'functionalityPartlyOk'
    INTERMITTENTLYOK = 'intermittentlyOk'
    ALARM = 'alarm'
    NOTRESPONDING = 'notResponding'
    OFFLINE = 'offline'
    UNKNOWN = 'unknown'
    EXTENDEDG = 'extendedG'
