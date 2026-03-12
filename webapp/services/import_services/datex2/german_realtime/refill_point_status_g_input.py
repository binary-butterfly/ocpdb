"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .electric_charging_point_status_input import ElectricChargingPointStatusInput
from .refill_point_status_input import RefillPointStatusInput


@validataclass
class RefillPointStatusGInput:
    aegiRefillPointStatus: RefillPointStatusInput | UnsetValueType = (
        DataclassValidator(RefillPointStatusInput),
        Default(UnsetValue),
    )
    aegiElectricChargingPointStatus: ElectricChargingPointStatusInput | UnsetValueType = (
        DataclassValidator(ElectricChargingPointStatusInput),
        Default(UnsetValue),
    )
