"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class FaultTypeEnum(Enum):
    INTERNALCOMMUNICATIONFAULT = 'internalCommunicationFault'
    SYNCHRONIZATIONFAULT = 'synchronizationFault'
    COMPONENTFAULT = 'componentFault'
    CONFIGURATIONERROR = 'configurationError'
    DISCONNECTED = 'disconnected'
    ELECTRONICSFAULT = 'electronicsFault'
    GENERALSYSTEMERROR = 'generalSystemError'
    HARDWAREFAULT = 'hardwareFault'
    CONTROLFAULT = 'controlFault'
    INTERMITTENTLYWORKING = 'intermittentlyWorking'
    MECHANICALFAULT = 'mechanicalFault'
    NOTWORKING = 'notWorking'
    OPERATINGSYSTEMFAULT = 'operatingSystemFault'
    POWERFAILURE = 'powerFailure'
    SECURITYFAULT = 'securityFault'
    SOFTWAREFAULT = 'softwareFault'
    TIMEORCLOCKFAULT = 'timeOrClockFault'
    UNSPECIFIEDFAULT = 'unspecifiedFault'
    UNKNOWNFAULT = 'unknownFault'
    OTHERFAULT = 'otherFault'
    EXTENDEDG = 'extendedG'
