"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class NamedAreaTypeEnum(Enum):
    APPLICATIONREGION = 'applicationRegion'
    CONTINENT = 'continent'
    COUNTRY = 'country'
    COUNTRYGROUP = 'countryGroup'
    CARPARKAREA = 'carParkArea'
    CARPOOLAREA = 'carpoolArea'
    FUZZYAREA = 'fuzzyArea'
    INDUSTRIALAREA = 'industrialArea'
    LAKE = 'lake'
    METEOROLOGICALAREA = 'meteorologicalArea'
    METROPOLITANAREA = 'metropolitanArea'
    MUNICIPALITY = 'municipality'
    PARKANDRIDESITE = 'parkAndRideSite'
    RURALCOUNTY = 'ruralCounty'
    SEA = 'sea'
    TOURISTAREA = 'touristArea'
    TRAFFICAREA = 'trafficArea'
    URBANCOUNTY = 'urbanCounty'
    ORDER1ADMINISTRATIVEAREA = 'order1AdministrativeArea'
    ORDER2ADMINISTRATIVEAREA = 'order2AdministrativeArea'
    ORDER3ADMINISTRATIVEAREA = 'order3AdministrativeArea'
    ORDER4ADMINISTRATIVEAREA = 'order4AdministrativeArea'
    ORDER5ADMINISTRATIVEAREA = 'order5AdministrativeArea'
    POLICEFORCECONTROLAREA = 'policeForceControlArea'
    ROADOPERATORCONTROLAREA = 'roadOperatorControlArea'
    WATERAREA = 'waterArea'
    EXTENDEDG = 'extendedG'
