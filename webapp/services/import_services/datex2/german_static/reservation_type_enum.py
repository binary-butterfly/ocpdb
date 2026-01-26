"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class ReservationTypeEnum(Enum):
    OPTIONAL = 'optional'
    MANDATORY = 'mandatory'
    NOTAVAILABLE = 'notAvailable'
    PARTLY = 'partly'
    UNKNOWN = 'unknown'
    UNSPECIFIED = 'unspecified'
    EXTENDEDG = 'extendedG'
