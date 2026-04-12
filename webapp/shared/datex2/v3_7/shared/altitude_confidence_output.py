"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .altitude_accuracy_enum_g_output import AltitudeAccuracyEnumGOutput
from .extension_type_g_output import ExtensionTypeGOutput
from .position_confidence_coded_error_enum_g_output import PositionConfidenceCodedErrorEnumGOutput


@dataclass(kw_only=True)
class AltitudeConfidenceOutput:
    altitudeAccuracyCodedValue: AltitudeAccuracyEnumGOutput | None = None
    altitudeAccuracyCodedError: PositionConfidenceCodedErrorEnumGOutput | None = None
    locAltitudeConfidenceExtensionG: ExtensionTypeGOutput | None = None
