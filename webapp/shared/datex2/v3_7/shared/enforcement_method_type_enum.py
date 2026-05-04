"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class EnforcementMethodTypeEnum(Enum):
    CAMERA = 'camera'
    MANUALSTICKERINSPECTION = 'manualStickerInspection'
    CHECKINGVEHICLEPAPERS = 'checkingVehiclePapers'
    MOBILELICENSEPLATECONTROLS = 'mobileLicensePlateControls'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
