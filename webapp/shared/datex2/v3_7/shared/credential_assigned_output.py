"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .credential_type_enum_g_output import CredentialTypeEnumGOutput
from .extension_type_g_output import ExtensionTypeGOutput
from .organisation_versioned_reference_g_output import OrganisationVersionedReferenceGOutput


@dataclass(kw_only=True)
class CredentialAssignedOutput:
    type: CredentialTypeEnumGOutput
    otherType: str | None = None
    localIdentifier: str | None = None
    issuer: OrganisationVersionedReferenceGOutput
    afacCredentialExtensionG: ExtensionTypeGOutput | None = None
    afacCredentialAssignedExtensionG: ExtensionTypeGOutput | None = None
