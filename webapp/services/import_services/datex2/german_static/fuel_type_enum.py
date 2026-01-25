"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class FuelTypeEnum(Enum):
    ALL = 'all'
    BATTERY = 'battery'
    BIODIESEL = 'biodiesel'
    DIESEL = 'diesel'
    DIESELBATTERYHYBRID = 'dieselBatteryHybrid'
    ETHANOL = 'ethanol'
    HYDROGEN = 'hydrogen'
    LIQUIDGAS = 'liquidGas'
    LPG = 'lpg'
    METHANE = 'methane'
    PETROL = 'petrol'
    PETROL95OCTANE = 'petrol95Octane'
    PETROL98OCTANE = 'petrol98Octane'
    PETROLBATTERYHYBRID = 'petrolBatteryHybrid'
    PETROLLEADED = 'petrolLeaded'
    PETROLUNLEADED = 'petrolUnleaded'
    UNKNOWN = 'unknown'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
