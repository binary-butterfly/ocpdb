"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator, StringValidator

from .address_input import AddressInput
from .nuts_area_input import NutsAreaInput


@validataclass
class FacilityLocationInput:
    timeZone: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    address: AddressInput | UnsetValueType = DataclassValidator(AddressInput), Default(UnsetValue)
    nutsArea: list[NutsAreaInput] | UnsetValueType = (
        ListValidator(DataclassValidator(NutsAreaInput)),
        Default(UnsetValue),
    )
