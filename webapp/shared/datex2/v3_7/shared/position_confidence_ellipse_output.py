"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .extension_type_g_output import ExtensionTypeGOutput
from .position_confidence_coded_error_enum_g_output import PositionConfidenceCodedErrorEnumGOutput


@dataclass(kw_only=True)
class PositionConfidenceEllipseOutput:
    semiMajorAxisLength: float | None = None
    semiMajorAxisLengthCodedError: PositionConfidenceCodedErrorEnumGOutput | None = None
    semiMinorAxisLength: float | None = None
    semiMinorAxisLengthCodedError: PositionConfidenceCodedErrorEnumGOutput | None = None
    semiMajorAxisOrientation: int | None = None
    semiMajorAxisOrientationError: bool | None = None
    locPositionConfidenceEllipseExtensionG: ExtensionTypeGOutput | None = None
