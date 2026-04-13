"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass
from datetime import datetime

from .closure_information_output import ClosureInformationOutput
from .extension_type_g_output import ExtensionTypeGOutput
from .overall_period_output import OverallPeriodOutput


@dataclass(kw_only=True)
class OperatingHoursSpecificationOutput:
    idG: str
    versionG: str
    lastUpdated: datetime | None = None
    label: str | None = None
    operatingAllYear: bool | None = None
    urlLinkAddress: str | None = None
    closureInformation: ClosureInformationOutput | None = None
    overallPeriod: OverallPeriodOutput
    afacOperatingHoursExtensionG: ExtensionTypeGOutput | None = None
    afacOperatingHoursSpecificationExtensionG: ExtensionTypeGOutput | None = None
