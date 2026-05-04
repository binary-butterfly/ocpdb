"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class ContactTypeEnum(Enum):
    OPERATOR = 'operator'
    OWNER = 'owner'
    EMERGENCYCONTACT = 'emergencyContact'
    SECURITYSERVICE = 'securityService'
    CUSTOMERSERVICE = 'customerService'
    PROPERTYMANAGER = 'propertyManager'
    RESERVATIONSERVICE = 'reservationService'
    RESPONSIBLEAUTHORITY = 'responsibleAuthority'
    SERVICEPARTNER = 'servicePartner'
    EXTENDEDG = 'extendedG'
