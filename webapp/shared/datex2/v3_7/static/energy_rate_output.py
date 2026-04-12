"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass
from datetime import datetime

from webapp.shared.datex2.v3_7.shared.energy_price_output import EnergyPriceOutput
from webapp.shared.datex2.v3_7.shared.extension_type_g_output import ExtensionTypeGOutput
from webapp.shared.datex2.v3_7.shared.multilingual_string_output import MultilingualStringOutput
from webapp.shared.datex2.v3_7.shared.overall_period_output import OverallPeriodOutput
from webapp.shared.datex2.v3_7.shared.payment_output import PaymentOutput

from .rate_policy_enum_g_output import RatePolicyEnumGOutput


@dataclass(kw_only=True)
class EnergyRateOutput:
    idG: str
    ratePolicy: RatePolicyEnumGOutput
    lastUpdated: datetime
    applicableCurrency: list[str]
    rateName: MultilingualStringOutput | None = None
    combinationWithParkingFee: bool | None = None
    maximumDeliveryFee: float | None = None
    minimumDeliveryFee: float | None = None
    discount: float | None = None
    additionalInformation: MultilingualStringOutput | None = None
    payment: PaymentOutput | None = None
    energyPrice: list[EnergyPriceOutput] | None = None
    overallPeriod: OverallPeriodOutput | None = None
    aegiEnergyRateExtensionG: ExtensionTypeGOutput | None = None
