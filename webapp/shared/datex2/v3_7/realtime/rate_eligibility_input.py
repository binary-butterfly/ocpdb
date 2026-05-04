"""
Copyright 2026 binary butterfly GmbH
Use of this source code is governed by an MIT-style license that can be found in the LICENSE.txt.
"""

from validataclass.dataclasses import Default, ValidataclassMixin, validataclass
from validataclass.helpers import UnsetValue, UnsetValueType
from validataclass.validators import BooleanValidator, DataclassValidator, IntegerValidator, ListValidator

from webapp.shared.datex2.v3_7.shared.extension_type_g_input import ExtensionTypeGInput
from webapp.shared.datex2.v3_7.shared.rate_discount_input import RateDiscountInput
from webapp.shared.datex2.v3_7.shared.right_specification_input import RightSpecificationInput

from .eligibility_input import EligibilityInput


@validataclass
class RateEligibilityInput(ValidataclassMixin):
    priority: int | UnsetValueType = IntegerValidator(), Default(UnsetValue)
    combinable: bool | UnsetValueType = BooleanValidator(), Default(UnsetValue)
    rateDiscount: RateDiscountInput | UnsetValueType = DataclassValidator(RateDiscountInput), Default(UnsetValue)
    eligibility: EligibilityInput = DataclassValidator(EligibilityInput)
    rightSpecification: list[RightSpecificationInput] | UnsetValueType = (
        ListValidator(DataclassValidator(RightSpecificationInput)),
        Default(UnsetValue),
    )
    facRateEligibilityExtensionG: ExtensionTypeGInput | UnsetValueType = (
        DataclassValidator(ExtensionTypeGInput),
        Default(UnsetValue),
    )
