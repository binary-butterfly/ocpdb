"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, StringValidator

from .electric_energy_source_type_enum_g_input import ElectricEnergySourceTypeEnumGInput
from .extension_type_g_input import ExtensionTypeGInput
from .percentage_value_input import PercentageValueInput


@validataclass
class ElectricEnergySourceRatioInput(ValidataclassMixin):
    """
    Ratio for the specified energy source
    """

    energySource: ElectricEnergySourceTypeEnumGInput = DataclassValidator(ElectricEnergySourceTypeEnumGInput)
    otherEnergySource: str | UnsetValueType = StringValidator(), Default(UnsetValue)
    sourceRatioValue: PercentageValueInput = DataclassValidator(PercentageValueInput)
    egiElectricEnergySourceRatioExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
