"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator, StringValidator

from .energy_pricing_policy_input import EnergyPricingPolicyInput
from .extension_type_g_input import ExtensionTypeGInput
from .overall_period_input import OverallPeriodInput
from .payment_method_input import PaymentMethodInput
from .rate_matrix_versioned_reference_g_input import RateMatrixVersionedReferenceGInput
from .rate_table_versioned_reference_g_input import RateTableVersionedReferenceGInput


@validataclass
class RatesByReferenceInput(ValidataclassMixin):
    applicableCurrency: list[str] | UnsetValueType = ListValidator(StringValidator()), Default(UnsetValue)
    rateTableReference: RateTableVersionedReferenceGInput = DataclassValidator(RateTableVersionedReferenceGInput)
    rateMatrixReference: RateMatrixVersionedReferenceGInput | UnsetValueType = (
        DataclassValidator(RateMatrixVersionedReferenceGInput),
        Default(UnsetValue),
    )
    paymentMethod: PaymentMethodInput | UnsetValueType = DataclassValidator(PaymentMethodInput), Default(UnsetValue)
    overallPeriod: OverallPeriodInput | UnsetValueType = DataclassValidator(OverallPeriodInput), Default(UnsetValue)
    energyPricingPolicy: EnergyPricingPolicyInput | UnsetValueType = (
        DataclassValidator(EnergyPricingPolicyInput),
        Default(UnsetValue),
    )
    facRatesExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    facRatesByReferenceExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
