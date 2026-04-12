"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from webapp.shared.datex2.v3_7.shared.energy_rate_reference_g_output import EnergyRateReferenceGOutput
from webapp.shared.datex2.v3_7.shared.extension_type_g_output import ExtensionTypeGOutput
from webapp.shared.datex2.v3_7.shared.multilingual_string_output import MultilingualStringOutput

from .energy_rate_output import EnergyRateOutput
from .organisation_g_output import OrganisationGOutput


@dataclass(kw_only=True)
class EnergyProductOutput:
    energyProductName: MultilingualStringOutput | None = None
    isGreenEnergy: bool | None = None
    energyRateByReference: list[EnergyRateReferenceGOutput] | None = None
    energyProductInformation: str | None = None
    renewableEnergyEvidence: str | None = None
    mobilityServiceProvider: list[OrganisationGOutput] | None = None
    energyRate: list[EnergyRateOutput] | None = None
    aegiEnergyProductExtensionG: ExtensionTypeGOutput | None = None
