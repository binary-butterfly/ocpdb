"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from webapp.shared.datex2.v3_7.shared.extension_type_g_output import ExtensionTypeGOutput
from webapp.shared.datex2.v3_7.shared.overall_period_output import OverallPeriodOutput

from .refill_point_status_enum_g_output import RefillPointStatusEnumGOutput


@dataclass(kw_only=True)
class PlannedRefillPointStatusOutput:
    status: RefillPointStatusEnumGOutput
    overallPeriod: OverallPeriodOutput
    aegiPlannedRefillPointStatusExtensionG: ExtensionTypeGOutput | None = None
