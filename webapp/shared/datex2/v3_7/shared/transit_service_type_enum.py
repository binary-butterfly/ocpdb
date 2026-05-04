"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class TransitServiceTypeEnum(Enum):
    AIR = 'air'
    BUS = 'bus'
    FERRY = 'ferry'
    HYDROFOIL = 'hydrofoil'
    RAIL = 'rail'
    TRAM = 'tram'
    UNDERGROUNDMETRO = 'undergroundMetro'
    EXTENDEDG = 'extendedG'
