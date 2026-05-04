"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class GasConnectorTypeEnum(Enum):
    GASEOUSHYDROGEN = 'gaseousHydrogen'
    LIQUIDHYDROGEN = 'liquidHydrogen'
    CNG = 'cng'
    LNG = 'lng'
    LPG = 'lpg'
    BIOGAS = 'biogas'
    UNKNOWN = 'unknown'
    EXTENDEDG = 'extendedG'
