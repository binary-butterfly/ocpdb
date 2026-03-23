"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class EmissionClassificationEuroEnum(Enum):
    EURO5 = 'euro5'
    EURO5A = 'euro5a'
    EURO5B = 'euro5b'
    EURO6 = 'euro6'
    EURO6A = 'euro6a'
    EURO6B = 'euro6b'
    EURO6C = 'euro6c'
    EUROV = 'euroV'
    EUROVI = 'euroVI'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
