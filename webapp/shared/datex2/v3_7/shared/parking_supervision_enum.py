"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class ParkingSupervisionEnum(Enum):
    REMOTE = 'remote'
    ONSITE = 'onSite'
    CONTROLCENTREONSITE = 'controlCentreOnSite'
    CONTROLCENTREOFFSITE = 'controlCentreOffSite'
    PATROL = 'patrol'
    NONE = 'none'
    UNKNOWN = 'unknown'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
