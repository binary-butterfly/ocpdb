"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .extension_type_g_output import ExtensionTypeGOutput
from .fuzzy_time_enum_g_output import FuzzyTimeEnumGOutput


@dataclass(kw_only=True)
class FuzzyPeriodOutput:
    beginOrDuration: FuzzyTimeEnumGOutput | None = None
    endOrDuration: FuzzyTimeEnumGOutput | None = None
    comxFuzzyPeriodExtensionG: ExtensionTypeGOutput | None = None
