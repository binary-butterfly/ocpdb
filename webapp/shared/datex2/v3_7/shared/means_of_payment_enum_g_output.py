"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .means_of_payment_enum import MeansOfPaymentEnum


@dataclass(kw_only=True)
class MeansOfPaymentEnumGOutput:
    value: MeansOfPaymentEnum
    extendedValueG: str | None = None
