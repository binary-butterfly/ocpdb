"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .address_line_output import AddressLineOutput
from .extension_type_g_output import ExtensionTypeGOutput
from .multilingual_string_output import MultilingualStringOutput


@dataclass(kw_only=True)
class AddressOutput:
    postcode: str | None = None
    city: MultilingualStringOutput | None = None
    countryCode: str | None = None
    addressLine: list[AddressLineOutput] | None = None
    locxAddressExtensionG: ExtensionTypeGOutput | None = None
