"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .payload_publication_g_output import PayloadPublicationGOutput


@dataclass(kw_only=True)
class DATEXII3D2PayloadOutput:
    payload: PayloadPublicationGOutput | None = None
