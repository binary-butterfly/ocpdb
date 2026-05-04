"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class PersonCategoryEnum(Enum):
    ADULT = 'adult'
    CHILD = 'child'
    EMERGENCYSERVICESPERSON = 'emergencyServicesPerson'
    FIREMAN = 'fireman'
    INFANT = 'infant'
    MEDICALSTAFF = 'medicalStaff'
    MEMBEROFTHEPUBLIC = 'memberOfThePublic'
    POLICEMAN = 'policeman'
    POLITICIAN = 'politician'
    PUBLICTRANSPORTPASSENGER = 'publicTransportPassenger'
    SICKPERSON = 'sickPerson'
    TRAFFICOFFICER = 'trafficOfficer'
    TRAFFICWARDEN = 'trafficWarden'
    VERYIMPORTANTPERSON = 'veryImportantPerson'
    EXTENDEDG = 'extendedG'
