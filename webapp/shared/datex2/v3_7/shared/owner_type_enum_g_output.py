"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .owner_type_enum import OwnerTypeEnum


@dataclass(kw_only=True)
class OwnerTypeEnumGOutput:
    value: OwnerTypeEnum
    extendedValueG: str | None = None
