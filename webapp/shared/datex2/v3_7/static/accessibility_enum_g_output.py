"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .accessibility_enum import AccessibilityEnum


@dataclass(kw_only=True)
class AccessibilityEnumGOutput:
    value: AccessibilityEnum
    extendedValueG: str | None = None
