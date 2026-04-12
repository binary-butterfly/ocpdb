"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .payment_mode_enum import PaymentModeEnum


@dataclass(kw_only=True)
class PaymentModeEnumGOutput:
    value: PaymentModeEnum
    extendedValueG: str | None = None
