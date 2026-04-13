"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .fault_type_enum import FaultTypeEnum


@dataclass(kw_only=True)
class FaultTypeEnumGOutput:
    value: FaultTypeEnum
    extendedValueG: str | None = None
