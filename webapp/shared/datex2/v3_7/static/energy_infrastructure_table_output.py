"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from webapp.shared.datex2.v3_7.shared.extension_type_g_output import ExtensionTypeGOutput

from .energy_infrastructure_site_output import EnergyInfrastructureSiteOutput


@dataclass(kw_only=True)
class EnergyInfrastructureTableOutput:
    idG: str
    versionG: str
    tableName: str | None = None
    energyInfrastructureSite: list[EnergyInfrastructureSiteOutput]
    aegiEnergyInfrastructureTableExtensionG: ExtensionTypeGOutput | None = None
