"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .opening_status_enum import OpeningStatusEnum


@dataclass(kw_only=True)
class OpeningStatusEnumGOutput:
    value: OpeningStatusEnum
    extendedValueG: str | None = None
