"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class StandingOrParkingConditionTypeEnum(Enum):
    ELECTRICVEHICLEDURINGCHARGING = 'electricVehicleDuringCharging'
    FOOTWAYALSO = 'footwayAlso'
    FOOTWAYONLY = 'footwayOnly'
    GETTINGINANDOUTOFAVEHICLE = 'gettingInAndOutOfAVehicle'
    KERBSIDEALSO = 'kerbsideAlso'
    KERBSIDEONLY = 'kerbsideOnly'
    LOADINGANDUNLOADING = 'loadingAndUnloading'
    VERGEALSO = 'vergeAlso'
    VERGEONLY = 'vergeOnly'
    EXTENDEDG = 'extendedG'
