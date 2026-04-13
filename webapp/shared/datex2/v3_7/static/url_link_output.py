"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from webapp.shared.datex2.v3_7.shared.extension_type_g_output import ExtensionTypeGOutput
from webapp.shared.datex2.v3_7.shared.multilingual_string_output import MultilingualStringOutput

from .url_link_type_enum_g_output import UrlLinkTypeEnumGOutput


@dataclass(kw_only=True)
class UrlLinkOutput:
    urlLinkAddress: str
    urlLinkDescription: MultilingualStringOutput | None = None
    urlLinkType: UrlLinkTypeEnumGOutput | None = None
    comUrlLinkExtensionG: ExtensionTypeGOutput | None = None
