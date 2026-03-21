"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class AddressLineTypeEnum(Enum):
    APARTMENT = 'apartment'
    BUILDING = 'building'
    POBOX = 'poBox'
    UNIT = 'unit'
    REGION = 'region'
    TOWN = 'town'
    DISTRICTTERRITORY = 'districtTerritory'
    FLOOR = 'floor'
    STREET = 'street'
    HOUSENUMBER = 'houseNumber'
    GENERALTEXTLINE = 'generalTextLine'
    EXTENDEDG = 'extendedG'
