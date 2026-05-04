"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class VmsTypeEnum(Enum):
    COLOURGRAPHIC = 'colourGraphic'
    ROTATINGPRISMSIGN = 'rotatingPrismSign'
    MONOCHROMEGRAPHIC = 'monochromeGraphic'
    SIMPLEMATRIXSIGN = 'simpleMatrixSign'
    FULLMATRIXSIGN = 'fullMatrixSign'
    ROLLERBLINDSIGN = 'rollerBlindSign'
    VIRTUALVMS = 'virtualVms'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
