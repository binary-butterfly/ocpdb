"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class AbnormalTrafficTypeEnum(Enum):
    STATIONARYTRAFFIC = 'stationaryTraffic'
    QUEUINGTRAFFIC = 'queuingTraffic'
    SLOWTRAFFIC = 'slowTraffic'
    HEAVYTRAFFIC = 'heavyTraffic'
    UNSPECIFIEDABNORMALTRAFFIC = 'unspecifiedAbnormalTraffic'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
