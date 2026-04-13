"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .energy_based_applicability_output import EnergyBasedApplicabilityOutput
from .extension_type_g_output import ExtensionTypeGOutput
from .multilingual_string_output import MultilingualStringOutput
from .overall_period_output import OverallPeriodOutput
from .price_type_enum_g_output import PriceTypeEnumGOutput
from .time_based_applicability_output import TimeBasedApplicabilityOutput


@dataclass(kw_only=True)
class EnergyPriceOutput:
    priceGroupIndex: int
    priceType: PriceTypeEnumGOutput
    value: float
    priceCap: float | None = None
    taxIncluded: bool | None = None
    taxRate: float | None = None
    additionalInformation: MultilingualStringOutput | None = None
    overallPeriod: OverallPeriodOutput | None = None
    timeBasedApplicability: TimeBasedApplicabilityOutput | None = None
    energyBasedApplicability: EnergyBasedApplicabilityOutput | None = None
    aegiEnergyPriceExtensionG: ExtensionTypeGOutput | None = None
