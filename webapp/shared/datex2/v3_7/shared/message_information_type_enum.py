"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class MessageInformationTypeEnum(Enum):
    CAMPAIGNMESSAGE = 'campaignMessage'
    DATETIME = 'dateTime'
    FUTUREINFORMATION = 'futureInformation'
    INSTRUCTIONORMESSAGE = 'instructionOrMessage'
    SITUATIONWARNING = 'situationWarning'
    TEMPERATURE = 'temperature'
    TRAFFICMANAGEMENT = 'trafficManagement'
    TRAVELTIME = 'travelTime'
    EXTENDEDG = 'extendedG'
