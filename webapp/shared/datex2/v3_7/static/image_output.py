"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from webapp.shared.datex2.v3_7.shared.extension_type_g_output import ExtensionTypeGOutput

from .image_format_enum_g_output import ImageFormatEnumGOutput


@dataclass(kw_only=True)
class ImageOutput:
    imageData: str
    imageFormat: ImageFormatEnumGOutput
    afacImageExtensionG: ExtensionTypeGOutput | None = None
