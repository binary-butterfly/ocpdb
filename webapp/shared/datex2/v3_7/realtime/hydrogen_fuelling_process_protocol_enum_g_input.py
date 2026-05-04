"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator, StringValidator

from .hydrogen_fuelling_process_protocol_enum import HydrogenFuellingProcessProtocolEnum


@validataclass
class HydrogenFuellingProcessProtocolEnumGInput(ValidataclassMixin):
    value: HydrogenFuellingProcessProtocolEnum = EnumValidator(HydrogenFuellingProcessProtocolEnum)
    extendedValueG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
