"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass
from datetime import datetime

from .extension_type_g_output import ExtensionTypeGOutput


@dataclass(kw_only=True)
class ClosureInformationOutput:
    permananentlyClosed: bool | None = None
    temporarilyClosed: bool | None = None
    closedFrom: datetime | None = None
    temporarilyClosedUntil: datetime | None = None
    afacClosureInformationExtensionG: ExtensionTypeGOutput | None = None
