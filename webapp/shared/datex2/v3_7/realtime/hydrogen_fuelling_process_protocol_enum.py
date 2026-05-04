"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class HydrogenFuellingProcessProtocolEnum(Enum):
    SAE2601V2010 = 'sae2601v2010'
    SAE2601V2014 = 'sae2601v2014'
    SAE2601V2016 = 'sae2601v2016'
    MCMETHOD = 'mcMethod'
    UNKNOWN = 'unknown'
    EXTENDEDG = 'extendedG'
