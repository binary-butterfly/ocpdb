"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from webapp.shared.datex2.v3_7.shared.extension_type_g_output import ExtensionTypeGOutput

from .type_of_identifier_enum_g_output import TypeOfIdentifierEnumGOutput


@dataclass(kw_only=True)
class ExternalIdentifierOutput:
    identifier: str
    typeOfIdentifier: TypeOfIdentifierEnumGOutput | None = None
    otherTypeOfIdentifier: str | None = None
    afacExternalIdentifierExtensionG: ExtensionTypeGOutput | None = None
