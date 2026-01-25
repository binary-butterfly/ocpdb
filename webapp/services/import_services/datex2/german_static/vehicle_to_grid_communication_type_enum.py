"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class VehicleToGridCommunicationTypeEnum(Enum):
    NONE = 'none'
    ISO15118 = 'iso15118'
    IEC619802 = 'iec619802'
    OTHER = 'other'
    UNKNOWN = 'unknown'
    EXTENDEDG = 'extendedG'
