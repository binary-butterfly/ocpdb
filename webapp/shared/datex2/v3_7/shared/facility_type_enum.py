"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class FacilityTypeEnum(Enum):
    AIRPORT = 'airport'
    CARPARK = 'carPark'
    CARRENTALSTATION = 'carRentalStation'
    ELECTRICCHARGINGSTATION = 'electricChargingStation'
    ENERGYINFRASTRUCTURESITE = 'energyInfrastructureSite'
    LORRYPARKINGSITE = 'lorryParkingSite'
    PARKINGSITE = 'parkingSite'
    PETROLSTATION = 'petrolStation'
    PUBLICTRANSPORTDEPOT = 'publicTransportDepot'
    PUBLICTRANSPORTHUB = 'publicTransportHub'
    SHOPPINGCENTRE = 'shoppingCentre'
    TRAINSTATION = 'trainStation'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
