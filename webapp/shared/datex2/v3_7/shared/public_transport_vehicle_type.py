"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class PublicTransportVehicleType(Enum):
    BUS = 'bus'
    COACH = 'coach'
    MINIBUS = 'miniBus'
    SUBWAY = 'subway'
    TAXI = 'taxi'
    TRAIN = 'train'
    TRAM = 'tram'
    EXTENDEDG = 'extendedG'
