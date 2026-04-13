"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .amount_in_currency_output import AmountInCurrencyOutput
from .extension_type_g_output import ExtensionTypeGOutput


@dataclass(kw_only=True)
class RateDiscountOutput:
    discountRate: float | None = None
    fixedValue: AmountInCurrencyOutput | None = None
    afacRateDiscountExtensionG: ExtensionTypeGOutput | None = None
