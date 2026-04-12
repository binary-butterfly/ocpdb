"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .credential_g_output import CredentialGOutput
from .extension_type_g_output import ExtensionTypeGOutput
from .multilingual_string_output import MultilingualStringOutput
from .referenceable_organisation_versioned_reference_g_output import ReferenceableOrganisationVersionedReferenceGOutput
from .right_type_enum_g_output import RightTypeEnumGOutput
from .validity_output import ValidityOutput


@dataclass(kw_only=True)
class RightSpecificationOutput:
    idG: str
    versionG: str
    type: RightTypeEnumGOutput | None = None
    description: list[MultilingualStringOutput] | None = None
    financialReference: str | None = None
    issuer: ReferenceableOrganisationVersionedReferenceGOutput | None = None
    transferable: bool | None = None
    transferableConditions: MultilingualStringOutput | None = None
    credential: list[CredentialGOutput] | None = None
    validity: ValidityOutput | None = None
    afacRightSpecificationExtensionG: ExtensionTypeGOutput | None = None
