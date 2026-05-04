"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class ParkingVacantSpacesEnum(Enum):
    NOPARKINGSPACESAVAILABLE = 'noParkingSpacesAvailable'
    EXPECTNOSPACESAVAILABLE = 'expectNoSpacesAvailable'
    ONLYAFEWSPACESAVAILABLE = 'onlyAFewSpacesAvailable'
    LESSTHAN10SPACESAVAILABLE = 'lessThan10SpacesAvailable'
    LESSTHAN20SPACESAVAILABLE = 'lessThan20SpacesAvailable'
    LESSTHAN30SPACESAVAILABLE = 'lessThan30SpacesAvailable'
    LESSTHAN40SPACESAVAILABLE = 'lessThan40SpacesAvailable'
    LESSTHAN50SPACESAVAILABLE = 'lessThan50SpacesAvailable'
    UNKNOWN = 'unknown'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
