"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import DataclassValidator, ListValidator, StringValidator

from .extension_type_g_input import ExtensionTypeGInput
from .overall_period_input import OverallPeriodInput
from .payment_input import PaymentInput
from .rate_matrix_versioned_reference_g_input import RateMatrixVersionedReferenceGInput


@validataclass
class RateMatrixByReferenceInput(ValidataclassMixin):
    applicableCurrency: list[str] | UnsetValueType = ListValidator(StringValidator()), Default(UnsetValue)
    rateTableReference: RateMatrixVersionedReferenceGInput = DataclassValidator(RateMatrixVersionedReferenceGInput)
    payment: PaymentInput | UnsetValueType = DataclassValidator(PaymentInput), Default(UnsetValue)
    overallPeriod: OverallPeriodInput | UnsetValueType = DataclassValidator(OverallPeriodInput), Default(UnsetValue)
    afacRatesExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
    afacRateMatrixByReferenceExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
