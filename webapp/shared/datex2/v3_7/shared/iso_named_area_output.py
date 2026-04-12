"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .extension_type_g_output import ExtensionTypeGOutput
from .multilingual_string_output import MultilingualStringOutput
from .named_area_extension_type_g_output import NamedAreaExtensionTypeGOutput
from .named_area_type_enum_g_output import NamedAreaTypeEnumGOutput
from .subdivision_type_enum_g_output import SubdivisionTypeEnumGOutput


@dataclass(kw_only=True)
class IsoNamedAreaOutput:
    areaName: MultilingualStringOutput
    namedAreaType: NamedAreaTypeEnumGOutput | None = None
    country: str | None = None
    subdivisionType: SubdivisionTypeEnumGOutput
    subdivisionCode: str
    comNamedAreaExtensionG: ExtensionTypeGOutput | None = None
    locNamedAreaExtensionG: NamedAreaExtensionTypeGOutput | None = None
    locIsoNamedAreaExtensionG: ExtensionTypeGOutput | None = None
