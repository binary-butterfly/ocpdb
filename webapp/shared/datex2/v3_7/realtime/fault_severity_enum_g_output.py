"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .fault_severity_enum import FaultSeverityEnum


@dataclass(kw_only=True)
class FaultSeverityEnumGOutput:
    value: FaultSeverityEnum
    extendedValueG: str | None = None
