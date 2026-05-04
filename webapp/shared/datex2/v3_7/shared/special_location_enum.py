"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class SpecialLocationEnum(Enum):
    AIRPORTTERMINAL = 'airportTerminal'
    EXHIBITONCENTRE = 'exhibitonCentre'
    SHOPPINGCENTRE = 'shoppingCentre'
    SPECIFICFACILITY = 'specificFacility'
    TRAINSTATION = 'trainStation'
    CAMPGROUND = 'campGround'
    THEMEPARK = 'themePark'
    FERRYTERMINAL = 'ferryTerminal'
    VEHICLEONRAILTERMINAL = 'vehicleOnRailTerminal'
    COACHSTATION = 'coachStation'
    CABLECARSTATION = 'cableCarStation'
    PUBLICTRANSPORTSTATION = 'publicTransportStation'
    MARKET = 'market'
    RELIGIOUSCENTRE = 'religiousCentre'
    CONVENTIONCENTRE = 'conventionCentre'
    CINEMA = 'cinema'
    SKILIFT = 'skiLift'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
