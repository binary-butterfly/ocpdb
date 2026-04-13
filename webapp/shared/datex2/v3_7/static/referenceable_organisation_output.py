"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass
from datetime import datetime

from webapp.shared.datex2.v3_7.shared.extension_type_g_output import ExtensionTypeGOutput
from webapp.shared.datex2.v3_7.shared.multilingual_string_output import MultilingualStringOutput
from webapp.shared.datex2.v3_7.shared.overall_period_output import OverallPeriodOutput

from .external_identifier_output import ExternalIdentifierOutput
from .organisation_type_enum_g_output import OrganisationTypeEnumGOutput
from .organisation_unit_output import OrganisationUnitOutput


@dataclass(kw_only=True)
class ReferenceableOrganisationOutput:
    idG: str
    versionG: str
    lastUpdated: datetime | None = None
    name: MultilingualStringOutput
    legalName: MultilingualStringOutput | None = None
    description: MultilingualStringOutput | None = None
    linkToGeneralInformation: str | None = None
    linkToLogo: str | None = None
    linkToWebform: str | None = None
    available24hours: bool | None = None
    responsibility: list[MultilingualStringOutput] | None = None
    publishingAgreement: bool | None = None
    type: OrganisationTypeEnumGOutput | None = None
    nationalOrganisationNumber: str | None = None
    nationalRegister: str | None = None
    vatIdentificationNumber: str | None = None
    generalTimeValidity: OverallPeriodOutput | None = None
    organisationUnit: list[OrganisationUnitOutput] | None = None
    externalIdentifier: list[ExternalIdentifierOutput] | None = None
    afacOrganisationExtensionG: ExtensionTypeGOutput | None = None
    afacAnOrganisationExtensionG: ExtensionTypeGOutput | None = None
    afacReferenceableOrganisationExtensionG: ExtensionTypeGOutput | None = None
