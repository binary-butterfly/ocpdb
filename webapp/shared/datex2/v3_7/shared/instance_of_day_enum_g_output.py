"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .instance_of_day_enum import InstanceOfDayEnum


@dataclass(kw_only=True)
class InstanceOfDayEnumGOutput:
    value: InstanceOfDayEnum
    extendedValueG: str | None = None
