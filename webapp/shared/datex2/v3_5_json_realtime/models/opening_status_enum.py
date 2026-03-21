"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class OpeningStatusEnum(Enum):
    OPEN = 'open'
    OPENWITHSERVICELIMITATION = 'openWithServiceLimitation'
    CLOSED = 'closed'
    CLOSEDONHOLIDAY = 'closedOnHoliday'
    CLOSEDONMAINTENANCE = 'closedOnMaintenance'
    TEMPORARILYCLOSED = 'temporarilyClosed'
    STATUSUNKNOWN = 'statusUnknown'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
