"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from webapp.shared.datex2.v3_7.shared.extension_type_g_output import ExtensionTypeGOutput
from webapp.shared.datex2.v3_7.shared.overall_period_output import OverallPeriodOutput
from webapp.shared.datex2.v3_7.shared.referenceable_organisation_versioned_reference_g_output import (
    ReferenceableOrganisationVersionedReferenceGOutput,
)

from .organisation_table_versioned_reference_g_output import OrganisationTableVersionedReferenceGOutput


@dataclass(kw_only=True)
class OrganisationByReferenceOutput:
    organisationReference: ReferenceableOrganisationVersionedReferenceGOutput
    organisationTableReference: OrganisationTableVersionedReferenceGOutput | None = None
    generalTimeValidity: OverallPeriodOutput | None = None
    afacOrganisationExtensionG: ExtensionTypeGOutput | None = None
    afacOrganisationByReferenceExtensionG: ExtensionTypeGOutput | None = None
