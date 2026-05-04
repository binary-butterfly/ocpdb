"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class HydrogenFuellingProcessProtocolEnum(Enum):
    SAEJ2601V2010 = 'saej2601v2010'
    SAEJ2601V2014 = 'saej2601v2014'
    SAEJ2601V2016 = 'saej2601v2016'
    MCMETHOD = 'mcMethod'
    UNKNOWN = 'unknown'
    EXTENDEDG = 'extendedG'
