"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class ElectricEnergySourceTypeEnum(Enum):
    BIOGAS = 'biogas'
    COAL = 'coal'
    GAS = 'gas'
    NUCLEAR = 'nuclear'
    SOLAR = 'solar'
    WATER = 'water'
    WIND = 'wind'
    GENERALGREEN = 'generalGreen'
    GENERALFOSSIL = 'generalFossil'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
