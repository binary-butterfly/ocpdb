"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import EnumValidator, StringValidator

from .traffic_regulation_order_status_enum import TrafficRegulationOrderStatusEnum


@validataclass
class TrafficRegulationOrderStatusEnumGInput(ValidataclassMixin):
    value: TrafficRegulationOrderStatusEnum = EnumValidator(TrafficRegulationOrderStatusEnum)
    extendedValueG: str | UnsetValueType = StringValidator(), Default(UnsetValue)
