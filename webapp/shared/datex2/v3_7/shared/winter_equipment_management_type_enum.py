"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class WinterEquipmentManagementTypeEnum(Enum):
    DONOTUSESTUDTYRES = 'doNotUseStudTyres'
    USESNOWCHAINS = 'useSnowChains'
    USESNOWCHAINSORTYRES = 'useSnowChainsOrTyres'
    USESNOWTYRES = 'useSnowTyres'
    WINTEREQUIPMENTONBOARDREQUIRED = 'winterEquipmentOnBoardRequired'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
