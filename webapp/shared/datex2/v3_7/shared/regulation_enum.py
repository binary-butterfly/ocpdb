"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class RegulationEnum(Enum):
    PERMITTED = 'permitted'
    PROHIBITED = 'prohibited'
    PUNISHABLE = 'punishable'
    SEASONALHETEROGENEOUS = 'seasonalHeterogeneous'
    PERMITTEDONLYATPARTICULARTIMES = 'permittedOnlyAtParticularTimes'
    PERMITTEDONLYONPARTICULARAREAS = 'permittedOnlyOnParticularAreas'
    PROHIBITEDATPARTICULARTIMES = 'prohibitedAtParticularTimes'
    PROHIBITEDONPARTICULARAREAS = 'prohibitedOnParticularAreas'
    ONLYONREQUEST = 'onlyOnRequest'
    HETEROGENEOUS = 'heterogeneous'
    ONLYOUTSIDEBUILDINGS = 'onlyOutsideBuildings'
    ONLYINSIDEBUILDINGS = 'onlyInsideBuildings'
    UNSPECIFIED = 'unspecified'
    UNKNOWN = 'unknown'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
