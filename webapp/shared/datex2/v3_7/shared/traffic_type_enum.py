"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class TrafficTypeEnum(Enum):
    ACCESSONLYTRAFFIC = 'accessOnlyTraffic'
    DESTINEDFORAIRPORT = 'destinedForAirport'
    DESTINEDFORAIRPORTARRIVALS = 'destinedForAirportArrivals'
    DESTINEDFORAIRPORTDEPARTURES = 'destinedForAirportDepartures'
    DESTINEDFORFERRYSERVICE = 'destinedForFerryService'
    DESTINEDFORRAILSERVICE = 'destinedForRailService'
    HOLIDAYTRAFFIC = 'holidayTraffic'
    LOCALTRAFFIC = 'localTraffic'
    LONGDISTANCETRAFFIC = 'longDistanceTraffic'
    REGIONALTRAFFIC = 'regionalTraffic'
    RESIDENTSONLYTRAFFIC = 'residentsOnlyTraffic'
    THROUGHTRAFFIC = 'throughTraffic'
    VISITORTRAFFIC = 'visitorTraffic'
    EXTENDEDG = 'extendedG'
