"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .address_output import AddressOutput
from .nuts_area_output import NutsAreaOutput


@dataclass(kw_only=True)
class AfirFacilityLocationOutput:
    timeZone: str | None = None
    address: AddressOutput | None = None
    nutsArea: list[NutsAreaOutput] | None = None
