"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from enum import Enum


class UrlLinkTypeEnum(Enum):
    DOCUMENTPDF = 'documentPdf'
    HTML = 'html'
    IMAGE = 'image'
    RSS = 'rss'
    VIDEOSTREAM = 'videoStream'
    VOICESTREAM = 'voiceStream'
    OTHER = 'other'
    EXTENDEDG = 'extendedG'
