"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .an_organisation_output import AnOrganisationOutput
from .organisation_by_reference_output import OrganisationByReferenceOutput
from .referenceable_organisation_output import ReferenceableOrganisationOutput
from .undefined_organisation_output import UndefinedOrganisationOutput
from .unknown_organisation_output import UnknownOrganisationOutput


@dataclass(kw_only=True)
class OrganisationGOutput:
    """
    Only one of the properties shall be used in an instance.
    """

    afacUndefinedOrganisation: UndefinedOrganisationOutput | None = None
    afacOrganisationByReference: OrganisationByReferenceOutput | None = None
    afacUnknownOrganisation: UnknownOrganisationOutput | None = None
    afacAnOrganisation: AnOrganisationOutput | None = None
    afacReferenceableOrganisation: ReferenceableOrganisationOutput | None = None
