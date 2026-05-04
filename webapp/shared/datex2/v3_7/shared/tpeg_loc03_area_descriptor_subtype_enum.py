"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class TpegLoc03AreaDescriptorSubtypeEnum(Enum):
    ADMINISTRATIVEAREANAME = 'administrativeAreaName'
    ADMINISTRATIVEREFERENCENAME = 'administrativeReferenceName'
    AREANAME = 'areaName'
    COUNTYNAME = 'countyName'
    LAKENAME = 'lakeName'
    NATIONNAME = 'nationName'
    POLICEFORCECONTROLAREANAME = 'policeForceControlAreaName'
    REGIONNAME = 'regionName'
    SEANAME = 'seaName'
    TOWNNAME = 'townName'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
