"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class RefillSolutionHydrogenEnum(Enum):
    GASEOUSHYDROGEN350BARCAR = 'gaseousHydrogen350barCar'
    GASEOUSHYDROGEN350BARTRUCK = 'gaseousHydrogen350barTruck'
    GASEOUSHYDROGEN700BARCAR = 'gaseousHydrogen700barCar'
    GASEOUSHYDROGEN700BARTRUCK = 'gaseousHydrogen700barTruck'
    LIQUIDHYDROGEN = 'liquidHydrogen'
    CRYOCOMPRESSEDHYDROGREN = 'cryoCompressedHydrogren'
    UNKNOWN = 'unknown'
    EXTENDEDG = 'extendedG'
