"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass
from datetime import datetime

from .extension_type_g_output import ExtensionTypeGOutput
from .period_output import PeriodOutput


@dataclass(kw_only=True)
class OverallPeriodOutput:
    overallStartTime: datetime
    overallEndTime: datetime | None = None
    validPeriod: list[PeriodOutput] | None = None
    exceptionPeriod: list[PeriodOutput] | None = None
    comOverallPeriodExtensionG: ExtensionTypeGOutput | None = None
