"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class GddServiceCategoryEnum(Enum):
    DANGERWARNING = 'dangerWarning'
    REGULATORY = 'regulatory'
    INFORMATIVE = 'informative'
    PUBLICFACILITIES = 'publicFacilities'
    AMBIENTCONDITIONS = 'ambientConditions'
    ROADCONDITIONS = 'roadConditions'
    EXTENDEDG = 'extendedG'
