"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class PriceTypeEnum(Enum):
    PRICEPERMINUTE = 'pricePerMinute'
    PRICEPERKWH = 'pricePerKWh'
    BASEPRICE = 'basePrice'
    FLATRATE = 'flatRate'
    FREE = 'free'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
