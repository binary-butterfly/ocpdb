"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .computation_method_enum import ComputationMethodEnum


@dataclass(kw_only=True)
class ComputationMethodEnumGOutput:
    value: ComputationMethodEnum
    extendedValueG: str | None = None
