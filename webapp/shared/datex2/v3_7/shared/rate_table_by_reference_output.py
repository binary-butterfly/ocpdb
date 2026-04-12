"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .extension_type_g_output import ExtensionTypeGOutput
from .overall_period_output import OverallPeriodOutput
from .payment_output import PaymentOutput
from .rate_table_versioned_reference_g_output import RateTableVersionedReferenceGOutput


@dataclass(kw_only=True)
class RateTableByReferenceOutput:
    applicableCurrency: list[str] | None = None
    rateReference: RateTableVersionedReferenceGOutput
    payment: PaymentOutput | None = None
    overallPeriod: OverallPeriodOutput | None = None
    afacRatesExtensionG: ExtensionTypeGOutput | None = None
    afacRateTableByReferenceExtensionG: ExtensionTypeGOutput | None = None
