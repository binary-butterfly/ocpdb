"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class EnergyInfrastructureSiteTypeEnum(Enum):
    INBUILDING = 'inBuilding'
    OPENSPACE = 'openSpace'
    ONSTREET = 'onstreet'
    ONCOMPANYSITE = 'onCompanySite'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
