"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .credential_type_enum_g_output import CredentialTypeEnumGOutput
from .extension_type_g_output import ExtensionTypeGOutput


@dataclass(kw_only=True)
class CredentialOutput:
    type: CredentialTypeEnumGOutput
    otherType: str | None = None
    afacCredentialExtensionG: ExtensionTypeGOutput | None = None
