"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .extension_type_g_output import ExtensionTypeGOutput


@dataclass(kw_only=True)
class RelativeOffsetsOutput:
    earliestStartRelative: str | None = None
    latestStartRelative: str | None = None
    earliestEndRelative: str | None = None
    latestEndRelative: str | None = None
    afacAssignedRightTimeRelativeExtensionG: ExtensionTypeGOutput | None = None
    afacRelativeOffsetsExtensionG: ExtensionTypeGOutput | None = None
