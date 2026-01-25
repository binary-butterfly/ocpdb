"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator, StringValidator

from .payment_mode_enum import PaymentModeEnum


@validataclass
class PaymentModeEnumGInput:
    value: PaymentModeEnum = EnumValidator(PaymentModeEnum)
    extendedValueG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
