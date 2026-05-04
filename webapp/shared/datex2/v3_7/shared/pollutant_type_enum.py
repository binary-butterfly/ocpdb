"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class PollutantTypeEnum(Enum):
    BENZENETOLUENEXYLENE = 'benzeneTolueneXylene'
    CARBONMONOXIDE = 'carbonMonoxide'
    LEAD = 'lead'
    METHANE = 'methane'
    NITRICOXIDE = 'nitricOxide'
    NITROGENDIOXIDE = 'nitrogenDioxide'
    NITROGENMONOXIDE = 'nitrogenMonoxide'
    NITROGENOXIDES = 'nitrogenOxides'
    NONMETHANEHYDROCARBONS = 'nonMethaneHydrocarbons'
    OZONE = 'ozone'
    PARTICULATES10 = 'particulates10'
    POLYCYCLICAROMATICHYDROCARBONS = 'polycyclicAromaticHydrocarbons'
    PRIMARYPARTICULATE = 'primaryParticulate'
    SULPHURDIOXIDE = 'sulphurDioxide'
    TOTALHYDROCARBONS = 'totalHydrocarbons'
    EXTENDEDG = 'extendedG'
