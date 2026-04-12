"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from webapp.shared.datex2.v3_7.shared.extension_type_g_output import ExtensionTypeGOutput


@dataclass(kw_only=True)
class DimensionOutput:
    length: float | None = None
    width: float | None = None
    height: float | None = None
    usableArea: int | None = None
    afacDimensionExtensionG: ExtensionTypeGOutput | None = None
