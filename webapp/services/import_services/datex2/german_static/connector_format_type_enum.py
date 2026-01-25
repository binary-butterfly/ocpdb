"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class ConnectorFormatTypeEnum(Enum):
    CABLEMODE2 = 'cableMode2'
    CABLEMODE3 = 'cableMode3'
    OTHERCABLE = 'otherCable'
    SOCKET = 'socket'
    EXTENDEDG = 'extendedG'
