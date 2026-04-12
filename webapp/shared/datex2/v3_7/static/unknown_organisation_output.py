"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from webapp.shared.datex2.v3_7.shared.extension_type_g_output import ExtensionTypeGOutput
from webapp.shared.datex2.v3_7.shared.overall_period_output import OverallPeriodOutput


@dataclass(kw_only=True)
class UnknownOrganisationOutput:
    generalTimeValidity: OverallPeriodOutput | None = None
    afacOrganisationExtensionG: ExtensionTypeGOutput | None = None
    afacUnknownOrganisationExtensionG: ExtensionTypeGOutput | None = None
