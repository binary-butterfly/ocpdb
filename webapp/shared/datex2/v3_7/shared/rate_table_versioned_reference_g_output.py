"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass


@dataclass(kw_only=True)
class RateTableVersionedReferenceGOutput:
    targetClass: str
    idG: str
    versionG: str | None = None
