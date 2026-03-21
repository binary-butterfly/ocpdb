"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class RefillPointStatusEnum(Enum):
    AVAILABLE = 'available'
    BLOCKED = 'blocked'
    CHARGING = 'charging'
    FAULTED = 'faulted'
    INOPERATIVE = 'inoperative'
    OCCUPIED = 'occupied'
    OUTOFORDER = 'outOfOrder'
    OUTOFSTOCK = 'outOfStock'
    PLANNED = 'planned'
    REMOVED = 'removed'
    RESERVED = 'reserved'
    UNAVAILABLE = 'unavailable'
    UNKNOWN = 'unknown'
    EXTENDEDG = 'extendedG'
