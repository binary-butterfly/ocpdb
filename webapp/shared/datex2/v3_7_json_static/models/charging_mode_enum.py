"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class ChargingModeEnum(Enum):
    MODE1AC1P = 'mode1AC1p'
    MODE1AC3P = 'mode1AC3p'
    MODE2AC1P = 'mode2AC1p'
    MODE2AC3P = 'mode2AC3p'
    MODE3AC3P = 'mode3AC3p'
    MODE4DC = 'mode4DC'
    LEGACYINDUCTIVE = 'legacyInductive'
    CCS = 'ccs'
    OTHER = 'other'
    UNKNOWN = 'unknown'
    EXTENDEDG = 'extendedG'
