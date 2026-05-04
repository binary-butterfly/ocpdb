"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class AccessEquipmentEnum(Enum):
    BARRIER = 'barrier'
    TRAFFICSIGNAL = 'trafficSignal'
    TICKETBUTTONMACHINE = 'ticketButtonMachine'
    TICKETCARDMACHINE = 'ticketCardMachine'
    PAYANDEXITMACHINE = 'payAndExitMachine'
    STAIRCASE = 'staircase'
    ELEVATOR = 'elevator'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
