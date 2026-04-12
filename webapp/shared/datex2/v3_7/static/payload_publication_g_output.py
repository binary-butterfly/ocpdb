"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .energy_infrastructure_table_publication_output import EnergyInfrastructureTablePublicationOutput


@dataclass(kw_only=True)
class PayloadPublicationGOutput:
    """
    Only one of the properties shall be used in an instance.
    """

    versionG: str | None = None
    modelBaseVersionG: str
    extensionNameG: str | None = None
    extensionVersionG: str | None = None
    profileNameG: str | None = None
    profileVersionG: str | None = None
    aegiEnergyInfrastructureTablePublication: EnergyInfrastructureTablePublicationOutput | None = None
