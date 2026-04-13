"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass
from datetime import datetime

from webapp.shared.datex2.v3_7.shared.energy_price_output import EnergyPriceOutput
from webapp.shared.datex2.v3_7.shared.energy_rate_reference_g_output import EnergyRateReferenceGOutput
from webapp.shared.datex2.v3_7.shared.extension_type_g_output import ExtensionTypeGOutput
from webapp.shared.datex2.v3_7.shared.multilingual_string_output import MultilingualStringOutput


@dataclass(kw_only=True)
class EnergyRateUpdateOutput:
    lastUpdated: datetime
    energyRateReference: EnergyRateReferenceGOutput
    additionalInformation: MultilingualStringOutput | None = None
    energyPrice: list[EnergyPriceOutput] | None = None
    aegiEnergyRateUpdateExtensionG: ExtensionTypeGOutput | None = None
