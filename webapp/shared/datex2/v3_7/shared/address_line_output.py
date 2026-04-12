"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .address_line_type_enum_g_output import AddressLineTypeEnumGOutput
from .extension_type_g_output import ExtensionTypeGOutput
from .multilingual_string_output import MultilingualStringOutput


@dataclass(kw_only=True)
class AddressLineOutput:
    order: int
    type: AddressLineTypeEnumGOutput
    text: MultilingualStringOutput
    locxAddressLineExtensionG: ExtensionTypeGOutput | None = None
