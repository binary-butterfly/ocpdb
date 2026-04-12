"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .image_format_enum import ImageFormatEnum


@dataclass(kw_only=True)
class ImageFormatEnumGOutput:
    value: ImageFormatEnum
    extendedValueG: str | None = None
