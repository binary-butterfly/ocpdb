"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class PricingPolicyEnum(Enum):
    PRICEPERCHARGINGTIME = 'pricePerChargingTime'
    PRICEPERDELIVERYUNIT = 'pricePerDeliveryUnit'
    CONTRACT = 'contract'
    FLATRATE = 'flatRate'
    UNKNOWN = 'unknown'
    FREE = 'free'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
