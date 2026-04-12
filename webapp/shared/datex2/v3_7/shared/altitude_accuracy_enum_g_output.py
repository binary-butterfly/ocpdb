"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .altitude_accuracy_enum import AltitudeAccuracyEnum


@dataclass(kw_only=True)
class AltitudeAccuracyEnumGOutput:
    value: AltitudeAccuracyEnum
    extendedValueG: str | None = None
