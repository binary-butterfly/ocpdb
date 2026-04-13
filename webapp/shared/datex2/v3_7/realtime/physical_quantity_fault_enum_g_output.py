"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .physical_quantity_fault_enum import PhysicalQuantityFaultEnum


@dataclass(kw_only=True)
class PhysicalQuantityFaultEnumGOutput:
    value: PhysicalQuantityFaultEnum
    extendedValueG: str | None = None
