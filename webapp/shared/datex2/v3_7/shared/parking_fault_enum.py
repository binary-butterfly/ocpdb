"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class ParkingFaultEnum(Enum):
    COMMUNICATIONSFAILURE = 'communicationsFailure'
    BARRIERMALFUNCTION = 'barrierMalfunction'
    ENTRANCEEXITOBSTRUCTED = 'entranceExitObstructed'
    ERRONEOUSOCCUPANCYINFORMATION = 'erroneousOccupancyInformation'
    ERRONEOUSOCCUPANCYDISPLAYED = 'erroneousOccupancyDisplayed'
    PAYMENTMACHINESINOPERATIVE = 'paymentMachinesInoperative'
    RESERVATIONSERVICEOUTOFORDER = 'reservationServiceOutOfOrder'
    NOPARKINGINFORMATIONAVAILABLE = 'noParkingInformationAvailable'
    UNSPECIFIED = 'unspecified'
    UNKNOWN = 'unknown'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
