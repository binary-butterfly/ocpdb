"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .extension_type_g_output import ExtensionTypeGOutput
from .multilingual_string_output import MultilingualStringOutput
from .named_area_extension_type_g_output import NamedAreaExtensionTypeGOutput
from .named_area_type_enum_g_output import NamedAreaTypeEnumGOutput
from .nuts_code_type_enum_g_output import NutsCodeTypeEnumGOutput


@dataclass(kw_only=True)
class NutsNamedAreaOutput:
    areaName: MultilingualStringOutput
    namedAreaType: NamedAreaTypeEnumGOutput | None = None
    country: str | None = None
    nutsCodeType: NutsCodeTypeEnumGOutput
    nutsCode: str
    comNamedAreaExtensionG: ExtensionTypeGOutput | None = None
    locNamedAreaExtensionG: NamedAreaExtensionTypeGOutput | None = None
    locNutsNamedAreaExtensionG: ExtensionTypeGOutput | None = None
