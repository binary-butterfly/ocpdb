"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class InformationTypeEnum(Enum):
    SITUATIONINFORMATION = 'situationInformation'
    WARNING = 'warning'
    PROHIBITION = 'prohibition'
    OBLIGATION = 'obligation'
    DESTINATION = 'destination'
    TRAVELTIME = 'travelTime'
    DELAY = 'delay'
    LOCATION = 'location'
    VEHICLETYPE = 'vehicleType'
    GENERALINFORMATION = 'generalInformation'
    BLANK = 'blank'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
