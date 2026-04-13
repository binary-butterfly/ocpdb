"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .refund_type_enum import RefundTypeEnum


@dataclass(kw_only=True)
class RefundTypeEnumGOutput:
    value: RefundTypeEnum
    extendedValueG: str | None = None
