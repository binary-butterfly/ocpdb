"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass
from datetime import datetime

from .extension_type_g_output import ExtensionTypeGOutput
from .international_identifier_output import InternationalIdentifierOutput
from .multilingual_string_output import MultilingualStringOutput
from .overall_period_output import OverallPeriodOutput
from .payment_output import PaymentOutput
from .rate_table_output import RateTableOutput


@dataclass(kw_only=True)
class RateMatrixOutput:
    idG: str
    versionG: str
    applicableCurrency: list[str] | None = None
    name: MultilingualStringOutput | None = None
    description: MultilingualStringOutput | None = None
    versionTime: datetime
    payment: PaymentOutput | None = None
    overallPeriod: OverallPeriodOutput | None = None
    informationManager: InternationalIdentifierOutput | None = None
    rateTable: list[RateTableOutput]
    afacRatesExtensionG: ExtensionTypeGOutput | None = None
    afacRateMatrixExtensionG: ExtensionTypeGOutput | None = None
