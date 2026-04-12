"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .extension_type_g_output import ExtensionTypeGOutput
from .overall_period_output import OverallPeriodOutput
from .payment_output import PaymentOutput


@dataclass(kw_only=True)
class FreeOfChargeOutput:
    applicableCurrency: list[str] | None = None
    payment: PaymentOutput | None = None
    overallPeriod: OverallPeriodOutput | None = None
    afacRatesExtensionG: ExtensionTypeGOutput | None = None
    afacFreeOfChargeExtensionG: ExtensionTypeGOutput | None = None
