"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class ChargingPointUsageTypeEnum(Enum):
    ELECTRICBOAT = 'electricBoat'
    ELECTRICBIKE = 'electricBike'
    ELECTRICALDEVICES = 'electricalDevices'
    ELECTRICMOTORCYCLE = 'electricMotorcycle'
    ELECTRICVEHICLE = 'electricVehicle'
    LORRYPOWERCONSUMPTION = 'lorryPowerConsumption'
    MOTORHOMEORCARAVANSUPPLY = 'motorhomeOrCaravanSupply'
    OVERHEADLINEDRIVENVEHICLES = 'overheadLineDrivenVehicles'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
