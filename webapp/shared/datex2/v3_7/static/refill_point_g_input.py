"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .alternative_fuels_refill_point_input import AlternativeFuelsRefillPointInput
from .diesel_refill_point_input import DieselRefillPointInput
from .electric_charging_point_input import ElectricChargingPointInput
from .petrol_refill_point_input import PetrolRefillPointInput


@validataclass
class RefillPointGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    aegiElectricChargingPoint: ElectricChargingPointInput | UnsetValueType = (
        DataclassValidator(ElectricChargingPointInput),
        Default(UnsetValue),
    )
    aegiPetrolRefillPoint: PetrolRefillPointInput | UnsetValueType = (
        DataclassValidator(PetrolRefillPointInput),
        Default(UnsetValue),
    )
    aegiDieselRefillPoint: DieselRefillPointInput | UnsetValueType = (
        DataclassValidator(DieselRefillPointInput),
        Default(UnsetValue),
    )
    aegiAlternativeFuelsRefillPoint: AlternativeFuelsRefillPointInput | UnsetValueType = (
        DataclassValidator(AlternativeFuelsRefillPointInput),
        Default(UnsetValue),
    )
