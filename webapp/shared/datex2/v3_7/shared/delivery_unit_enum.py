"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class DeliveryUnitEnum(Enum):
    LITRE = 'litre'
    KWH = 'kWh'
    KG = 'kg'
    M3 = 'm3'
    IMPERIALGALLON = 'imperialGallon'
    USGALLON = 'usGallon'
    GASGALLONEQUIVALENT = 'gasGallonEquivalent'
    EXTENDEDG = 'extendedG'
