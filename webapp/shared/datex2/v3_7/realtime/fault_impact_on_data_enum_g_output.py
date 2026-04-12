"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .fault_impact_on_data_enum import FaultImpactOnDataEnum


@dataclass(kw_only=True)
class FaultImpactOnDataEnumGOutput:
    value: FaultImpactOnDataEnum
    extendedValueG: str | None = None
