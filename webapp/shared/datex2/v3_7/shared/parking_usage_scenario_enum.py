"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class ParkingUsageScenarioEnum(Enum):
    AUTOMATEDPARKINGGARAGE = 'automatedParkingGarage'
    CARSHARING = 'carSharing'
    DELIVERY = 'delivery'
    DROPOFF = 'dropOff'
    DROPOFFMECHANICAL = 'dropOffMechanical'
    DROPOFFWITHVALET = 'dropOffWithValet'
    EVENTPARKING = 'eventParking'
    GUIDANCETOAVAILABLESPACES = 'guidanceToAvailableSpaces'
    KISSANDRIDE = 'kissAndRide'
    LIFTSHARE = 'liftshare'
    MOTORWAYPARKING = 'motorwayParking'
    NEARBYMOTORWAYPARKING = 'nearbyMotorwayParking'
    OVERNIGHTPARKING = 'overnightParking'
    PARKANDCYCLE = 'parkAndCycle'
    PARKANDDRIVE = 'parkAndDrive'
    PARKANDRIDE = 'parkAndRide'
    PARKANDWALK = 'parkAndWalk'
    POIPARKING = 'poiParking'
    RESTAREA = 'restArea'
    SERVICEAREA = 'serviceArea'
    SPECIALLOCATION = 'specialLocation'
    STAFFGUIDESTOSPACE = 'staffGuidesToSpace'
    TRUCKPARKING = 'truckParking'
    VEHICLELIFT = 'vehicleLift'
    ZONE = 'zone'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
