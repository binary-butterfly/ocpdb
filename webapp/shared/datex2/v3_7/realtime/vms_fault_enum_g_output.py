"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .vms_fault_enum import VmsFaultEnum


@dataclass(kw_only=True)
class VmsFaultEnumGOutput:
    value: VmsFaultEnum
    extendedValueG: str | None = None
