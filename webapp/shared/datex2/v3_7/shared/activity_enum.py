"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class ActivityEnum(Enum):
    OPENFIRE = 'openFire'
    OVERNIGHTPARKING = 'overnightParking'
    PICNIC = 'picnic'
    SMOKING = 'smoking'
    CAMPING = 'camping'
    HANDLINGHAZARDOUSMATERIAL = 'handlingHazardousMaterial'
    BARBECUE = 'barbecue'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
