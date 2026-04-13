"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass
from datetime import datetime

from webapp.shared.datex2.v3_7.shared.extension_type_g_output import ExtensionTypeGOutput
from webapp.shared.datex2.v3_7.shared.header_information_output import HeaderInformationOutput
from webapp.shared.datex2.v3_7.shared.international_identifier_output import InternationalIdentifierOutput
from webapp.shared.datex2.v3_7.shared.multilingual_string_output import MultilingualStringOutput

from .energy_infrastructure_table_output import EnergyInfrastructureTableOutput


@dataclass(kw_only=True)
class EnergyInfrastructureTablePublicationOutput:
    lang: str
    feedDescription: MultilingualStringOutput | None = None
    feedType: str | None = None
    publicationTime: datetime
    publicationCreator: InternationalIdentifierOutput
    headerInformation: HeaderInformationOutput | None = None
    energyInfrastructureTable: list[EnergyInfrastructureTableOutput]
    comPayloadPublicationExtensionG: ExtensionTypeGOutput | None = None
    aegiEnergyInfrastructureTablePublicationExtensionG: ExtensionTypeGOutput | None = None
