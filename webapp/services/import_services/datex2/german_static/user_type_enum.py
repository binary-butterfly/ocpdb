"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class UserTypeEnum(Enum):
    ALLUSERS = 'allUsers'
    COMMUTERS = 'commuters'
    CUSTOMERS = 'customers'
    ELDERLYUSERS = 'elderlyUsers'
    EMPLOYEES = 'employees'
    FAMILIES = 'families'
    PERSONSWITHDISABILITIES = 'personsWithDisabilities'
    HEARINGIMPAIRED = 'hearingImpaired'
    HOTELGUESTS = 'hotelGuests'
    LONGTERMPARKERS = 'longTermParkers'
    MEMBERS = 'members'
    MEN = 'men'
    OVERNIGHTPARKERS = 'overnightParkers'
    PARKANDCYCLEUSER = 'parkAndCycleUser'
    PARKANDRIDEUSERS = 'parkAndRideUsers'
    PARKANDWALKUSER = 'parkAndWalkUser'
    PENSIONERS = 'pensioners'
    PREGNANTPERSON = 'pregnantPerson'
    REGISTEREDDISABLEDUSERS = 'registeredDisabledUsers'
    RESERVATIONHOLDERS = 'reservationHolders'
    RESIDENTS = 'residents'
    SEASONTICKETHOLDERS = 'seasonTicketHolders'
    SHOPPERS = 'shoppers'
    SHORTTERMPARKERS = 'shortTermParkers'
    SPORTEVENTAWAYSUPPORTERS = 'sportEventAwaySupporters'
    SPORTEVENTHOMESUPPORTERS = 'sportEventHomeSupporters'
    STUDENTS = 'students'
    STAFF = 'staff'
    SUBSCRIBERS = 'subscribers'
    VISITORS = 'visitors'
    VISUALLYIMPAIRED = 'visuallyImpaired'
    WHEELCHAIRUSERS = 'wheelchairUsers'
    WOMEN = 'women'
    UNKNOWN = 'unknown'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
