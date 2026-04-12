"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .extension_type_g_output import ExtensionTypeGOutput
from .multilingual_string_output import MultilingualStringOutput


@dataclass(kw_only=True)
class RateLineTaxOutput:
    taxValue: float | None = None
    taxRate: float | None = None
    taxIncluded: bool
    trigger: MultilingualStringOutput | None = None
    labelForDisplay: MultilingualStringOutput | None = None
    afacRateLineTaxExtensionG: ExtensionTypeGOutput | None = None
