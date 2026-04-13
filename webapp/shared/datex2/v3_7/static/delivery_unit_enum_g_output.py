"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from dataclasses import dataclass

from .delivery_unit_enum import DeliveryUnitEnum


@dataclass(kw_only=True)
class DeliveryUnitEnumGOutput:
    value: DeliveryUnitEnum
    extendedValueG: str | None = None
