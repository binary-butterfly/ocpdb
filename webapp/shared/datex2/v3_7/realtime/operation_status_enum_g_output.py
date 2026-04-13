"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .operation_status_enum import OperationStatusEnum


@dataclass(kw_only=True)
class OperationStatusEnumGOutput:
    value: OperationStatusEnum
    extendedValueG: str | None = None
