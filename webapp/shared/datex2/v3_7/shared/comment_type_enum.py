"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class CommentTypeEnum(Enum):
    ABNORMALLOADMOVEMENTNOTE = 'abnormalLoadMovementNote'
    DATAPROCESSINGNOTE = 'dataProcessingNote'
    DESCRIPTION = 'description'
    INTERNALNOTE = 'internalNote'
    ROADWORKSNAME = 'roadworksName'
    WARNING = 'warning'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
