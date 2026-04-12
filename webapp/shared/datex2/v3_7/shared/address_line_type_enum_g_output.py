"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .address_line_type_enum import AddressLineTypeEnum


@dataclass(kw_only=True)
class AddressLineTypeEnumGOutput:
    value: AddressLineTypeEnum
    extendedValueG: str | None = None
