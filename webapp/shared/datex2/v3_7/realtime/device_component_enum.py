"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class DeviceComponentEnum(Enum):
    AMBIENTLIGHTMONITOR = 'ambientLightMonitor'
    CABINET = 'cabinet'
    COMMUNICATIONSEQUIPMENT = 'communicationsEquipment'
    CONTROLLER = 'controller'
    DISPLAY = 'display'
    FAN = 'fan'
    GENERALPURPOSEIOPORT = 'generalPurposeIoPort'
    HEATER = 'heater'
    OTHER = 'other'
    POWERSUPPLY = 'powerSupply'
    PROCESSOR = 'processor'
    SENSOR = 'sensor'
    EXTENDEDG = 'extendedG'
