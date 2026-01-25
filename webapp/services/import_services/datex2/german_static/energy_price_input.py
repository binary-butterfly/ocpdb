"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator, FloatValidator

from .energy_based_applicability_input import EnergyBasedApplicabilityInput
from .extension_type_g_input import ExtensionTypeGInput
from .multilingual_string_input import MultilingualStringInput
from .overall_period_input import OverallPeriodInput
from .price_type_enum_g_input import PriceTypeEnumGInput
from .time_based_applicability_input import TimeBasedApplicabilityInput


@validataclass
class EnergyPriceInput:
    priceType: PriceTypeEnumGInput = DataclassValidator(PriceTypeEnumGInput)
    value: int = FloatValidator()
    priceCap: int | UnsetValueType = FloatValidator(), Default(UnsetValue)
    taxIncluded: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    taxRate: int | UnsetValueType = FloatValidator(), Default(UnsetValue)
    additionalInformation: MultilingualStringInput | UnsetValueType = (
        DataclassValidator(MultilingualStringInput),
        Default(UnsetValue),
    )
    overallPeriod: OverallPeriodInput | UnsetValueType = DataclassValidator(OverallPeriodInput), Default(UnsetValue)
    timeBasedApplicability: TimeBasedApplicabilityInput | UnsetValueType = (
        DataclassValidator(TimeBasedApplicabilityInput),
        Default(UnsetValue),
    )
    energyBasedApplicability: EnergyBasedApplicabilityInput | UnsetValueType = (
        DataclassValidator(EnergyBasedApplicabilityInput),
        Default(UnsetValue),
    )
    aegiEnergyPriceExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
