"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class PhysicalSupportEnum(Enum):
    CENTRALRESERVATIONMOUNTED = 'centralReservationMounted'
    GANTRYMOUNTED = 'gantryMounted'
    OVERHEADBRIDGEMOUNTED = 'overheadBridgeMounted'
    ROADSIDECANTILEVERMOUNTED = 'roadsideCantileverMounted'
    ROADSIDEMOUNTED = 'roadsideMounted'
    TRAILERMOUNTED = 'trailerMounted'
    TUNNELENTRANCEMOUNTED = 'tunnelEntranceMounted'
    VEHICLEMOUNTED = 'vehicleMounted'
    EXTENDEDG = 'extendedG'
