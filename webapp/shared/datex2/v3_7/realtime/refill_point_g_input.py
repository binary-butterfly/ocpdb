"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator

from .diesel_refill_point_input import DieselRefillPointInput
from .electric_charging_point_input import ElectricChargingPointInput
from .hydrogen_refill_point_input import HydrogenRefillPointInput
from .organic_gas_refill_point_input import OrganicGasRefillPointInput
from .petrol_refill_point_input import PetrolRefillPointInput


@validataclass
class RefillPointGInput(ValidataclassMixin):
    """
    Only one of the properties shall be used in an instance.
    """

    egiHydrogenRefillPoint: HydrogenRefillPointInput | UnsetValueType = (
        DataclassValidator(HydrogenRefillPointInput),
        Default(UnsetValue),
    )
    egiPetrolRefillPoint: PetrolRefillPointInput | UnsetValueType = (
        DataclassValidator(PetrolRefillPointInput),
        Default(UnsetValue),
    )
    egiOrganicGasRefillPoint: OrganicGasRefillPointInput | UnsetValueType = (
        DataclassValidator(OrganicGasRefillPointInput),
        Default(UnsetValue),
    )
    egiElectricChargingPoint: ElectricChargingPointInput | UnsetValueType = (
        DataclassValidator(ElectricChargingPointInput),
        Default(UnsetValue),
    )
    egiDieselRefillPoint: DieselRefillPointInput | UnsetValueType = (
        DataclassValidator(DieselRefillPointInput),
        Default(UnsetValue),
    )
