"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .information_status_enum import InformationStatusEnum


@dataclass(kw_only=True)
class InformationStatusEnumGOutput:
    value: InformationStatusEnum
    extendedValueG: str | None = None
