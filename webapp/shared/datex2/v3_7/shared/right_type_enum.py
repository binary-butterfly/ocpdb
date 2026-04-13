"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class RightTypeEnum(Enum):
    ONETIMEUSEPARKING = 'oneTimeUseParking'
    PERMITPARKING = 'permitParking'
    LOADINGUNLOADING = 'loadingUnloading'
    SETDOWNPICKUP = 'setdownPickup'
    WAITING = 'waiting'
    ACCESSPERMISSION = 'accessPermission'
    DOINGRESERVATION = 'doingReservation'
    ELECTRICCHARGING = 'electricCharging'
    EXTENDEDG = 'extendedG'
