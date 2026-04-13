"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .vms_controller_fault_enum import VmsControllerFaultEnum


@dataclass(kw_only=True)
class VmsControllerFaultEnumGOutput:
    value: VmsControllerFaultEnum
    extendedValueG: str | None = None
