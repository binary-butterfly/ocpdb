"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .user_type_enum import UserTypeEnum


@dataclass(kw_only=True)
class UserTypeEnumGOutput:
    value: UserTypeEnum
    extendedValueG: str | None = None
