"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .position_confidence_coded_error_enum import PositionConfidenceCodedErrorEnum


@dataclass(kw_only=True)
class PositionConfidenceCodedErrorEnumGOutput:
    value: PositionConfidenceCodedErrorEnum
    extendedValueG: str | None = None
