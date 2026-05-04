"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class GddServiceCategoryEnum(Enum):
    AMBIENTCONDITIONS = 'ambientConditions'
    DANGERWARNING = 'dangerWarning'
    INFORMATIVE = 'informative'
    PUBLICFACILITIES = 'publicFacilities'
    REGULATORY = 'regulatory'
    ROADCONDITIONS = 'roadConditions'
    EXTENDEDG = 'extendedG'
