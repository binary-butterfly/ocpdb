"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from webapp.shared.datex2.v3_7.shared.extension_type_g_output import ExtensionTypeGOutput


@dataclass(kw_only=True)
class ContactInformationOutput:
    language: list[str] | None = None
    telephoneNumber: str | None = None
    faxNumber: str | None = None
    eMail: str | None = None
    afacContactInformationExtensionG: ExtensionTypeGOutput | None = None
