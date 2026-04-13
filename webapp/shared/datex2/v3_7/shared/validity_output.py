"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .extension_type_g_output import ExtensionTypeGOutput
from .overall_period_output import OverallPeriodOutput
from .validity_status_enum_g_output import ValidityStatusEnumGOutput


@dataclass(kw_only=True)
class ValidityOutput:
    validityStatus: ValidityStatusEnumGOutput
    overrunning: bool | None = None
    validityTimeSpecification: OverallPeriodOutput
    comValidityExtensionG: ExtensionTypeGOutput | None = None
