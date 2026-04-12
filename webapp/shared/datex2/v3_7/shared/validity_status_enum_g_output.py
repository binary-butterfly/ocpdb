"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .validity_status_enum import ValidityStatusEnum


@dataclass(kw_only=True)
class ValidityStatusEnumGOutput:
    value: ValidityStatusEnum
    extendedValueG: str | None = None
