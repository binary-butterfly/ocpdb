"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class DelaysTypeEnum(Enum):
    DELAYS = 'delays'
    DELAYSOFUNCERTAINDURATION = 'delaysOfUncertainDuration'
    LONGDELAYS = 'longDelays'
    VERYLONGDELAYS = 'veryLongDelays'
    EXTENDEDG = 'extendedG'
